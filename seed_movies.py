#!/usr/bin/env python3
"""Stream the approved movie dataset into an Autonomous Database MongoDB API collection.

The source dataset is newline-delimited JSON (NDJSON). Documents are upserted by
``movie_id`` so the script can be run repeatedly without creating duplicates.
Existing fields that are not part of the source, including ``summary_embedding``,
are preserved for the later vector-search tasks.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Iterator
from typing import Any
from urllib.request import Request, urlopen

from pymongo import MongoClient, UpdateOne
from pymongo.errors import PyMongoError


DEFAULT_SOURCE_URL = (
    "https://objectstorage.us-ashburn-1.oraclecloud.com/"
    "n/c4u04/b/moviestream_landing/o/movie/movies.json"
)
DEFAULT_DATABASE = "movies"
DEFAULT_COLLECTION = "movies"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load the LiveLabs movie dataset through the MongoDB API."
    )
    parser.add_argument(
        "--source-url",
        default=DEFAULT_SOURCE_URL,
        help="NDJSON movie source URL (default: approved Oracle Object Storage source).",
    )
    parser.add_argument(
        "--database",
        default=os.getenv("MONGODB_DATABASE", DEFAULT_DATABASE),
        help=f"MongoDB database/schema (default: ${'{'}MONGODB_DATABASE:-{DEFAULT_DATABASE}{'}'}).",
    )
    parser.add_argument(
        "--collection",
        default=os.getenv("MONGODB_COLLECTION", DEFAULT_COLLECTION),
        help=(
            f"MongoDB collection (default: "
            f"${'{'}MONGODB_COLLECTION:-{DEFAULT_COLLECTION}{'}'})."
        ),
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=250,
        help="Documents to write per bulk operation (default: 250).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Load only this many source documents; useful for a quick test.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and count source documents without connecting to MongoDB.",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop the target collection before loading. Use only for a fresh workshop reset.",
    )
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.reset and args.dry_run:
        parser.error("--reset cannot be used with --dry-run")
    return args


def stream_movies(source_url: str) -> Iterator[dict[str, Any]]:
    request = Request(source_url, headers={"User-Agent": "livelabs-movie-seeder/1.0"})
    with urlopen(request, timeout=60) as response:
        for line_number, raw_line in enumerate(response, start=1):
            line = raw_line.decode("utf-8").strip()
            if not line:
                continue
            try:
                movie = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Source line {line_number} is not valid JSON: {error.msg}"
                ) from error
            if not isinstance(movie, dict):
                raise ValueError(f"Source line {line_number} must contain a JSON object.")
            if movie.get("movie_id") is None:
                raise ValueError(f"Source line {line_number} is missing movie_id.")
            yield movie


def flush_batch(collection: Any, batch: list[UpdateOne]) -> int:
    if not batch:
        return 0
    collection.bulk_write(batch, ordered=False)
    return len(batch)


def main() -> int:
    args = parse_args()
    mongo_uri = os.getenv("MONGODB_URI")
    if not args.dry_run and not mongo_uri:
        print("MONGODB_URI is required unless --dry-run is used.", file=sys.stderr)
        return 2

    client: MongoClient | None = None
    collection: Any = None
    loaded = 0
    batch: list[UpdateOne] = []

    try:
        if not args.dry_run:
            client = MongoClient(mongo_uri, serverSelectionTimeoutMS=15_000)
            client.admin.command("ping")
            collection = client[args.database][args.collection]
            if args.reset:
                collection.drop()
                print(f"Dropped {args.database}.{args.collection} for a fresh load.")

        for movie in stream_movies(args.source_url):
            loaded += 1
            if not args.dry_run:
                # $set does not remove fields absent from the source. This preserves
                # summary_embedding when the seed script is rerun after Module 3.
                batch.append(
                    UpdateOne({"movie_id": movie["movie_id"]}, {"$set": movie}, upsert=True)
                )
                if len(batch) >= args.batch_size:
                    flush_batch(collection, batch)
                    batch.clear()
            if args.limit is not None and loaded >= args.limit:
                break

        if not args.dry_run:
            flush_batch(collection, batch)
            print(
                f"Loaded or updated {loaded} movies in "
                f"{args.database}.{args.collection}."
            )
        else:
            print(f"Validated {loaded} movie documents from {args.source_url}.")
        return 0
    except (OSError, ValueError, PyMongoError) as error:
        print(f"Seed failed: {error}", file=sys.stderr)
        return 1
    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    raise SystemExit(main())
