# Workshop Details

## Title

Search Using MongoDB API for Oracle AI Database

## Authoring Status

- Mode: Draft
- Variants: Sandbox and Tenancy
- Estimated workshop time: 75 minutes
- Audience: Database developers and platform engineers

## Short Description

Load a movie collection into Oracle Autonomous AI Database, query the same documents from SQL and `mongosh`, and build keyword and semantic searches with an in-database ONNX embedding model.

## Long Description

This workshop starts with the learner signing in to either a LiveLabs Sandbox or their own OCI tenancy. Participants open an Oracle Autonomous AI Database, install `mongosh` in OCI Cloud Shell, retrieve the MongoDB API connection string, verify the connection, load a sample movie collection from Oracle Object Storage, and query the same documents through SQL and `mongosh`.

Participants load an in-database ONNX model and verify that it generates an embedding. They then add summary embeddings to the movie documents, create text and vector search indexes, and compare keyword, semantic, and combined search patterns.

## Prerequisites

- A LiveLabs Sandbox reservation or an OCI free or paid tenancy
- An Autonomous AI Database with MongoDB API enabled
- An Autonomous AI Database administrator who can enable `mongo.preview` for the tenancy variant
- A nonproduction database account with MongoDB API access and the required `DBMS_CLOUD` and `DBMS_VECTOR` privileges
- Access to the OCI Console, Database Actions SQL, and OCI Cloud Shell
- A MongoDB API connection string for the workshop database account
- The provided multilingual E5-base ONNX model URL

## Sandbox Environment Contract

The workshop environment must provide each learner with:

- OCI login credentials and the database `ADMIN` password under **View Login Info**
- One SQL worksheet connected to the learner's schema
- OCI Cloud Shell with outbound access to the official MongoDB Shell download URL
- A MongoDB API connection string for the same schema
- Network access to the Autonomous AI Database MongoDB API endpoint
- A clean `ADMIN` schema in which `MOVIES` does not yet exist
- Access to the public movie dataset URL used in Lab 1
- The provided multilingual E5-base ONNX model URL for `DBMS_VECTOR.LOAD_ONNX_MODEL_CLOUD`

## Tenancy Environment Contract

The tenancy variant requires the learner to provide:

- An OCI free or paid tenancy and access to the OCI Console
- An Autonomous AI Database with the MongoDB API enabled
- Autonomous AI Database administrator credentials to set `mongo.preview` to lowercase `true`
- A nonproduction schema that can use `DBMS_CLOUD.COPY_COLLECTION` and `DBMS_VECTOR.LOAD_ONNX_MODEL_CLOUD`
- The database user's password and MongoDB API access URL
- OCI Cloud Shell access and network access from Cloud Shell to the database MongoDB API endpoint
- The provided multilingual E5-base ONNX model URL for `DBMS_VECTOR.LOAD_ONNX_MODEL_CLOUD`

## Workshop Outline

1. Introduction - 5 minutes
2. Get Started: Access the LiveLabs Sandbox or Your OCI Tenancy - 15 minutes
3. Lab 1: Load and Verify the Search Environment - 20 minutes
4. Lab 2: Prepare Search and Run a Keyword Query - 15 minutes
5. Lab 3: Run Semantic and Combined Searches - 20 minutes

## Lab 1 Completion Checkpoint

Lab 1 is complete only when the learner can show:

1. Movie rows returned from a SQL query against `MOVIES`.
2. Movie documents returned from a `mongosh` query against `db.MOVIES`.
3. A 768-dimension vector returned by `VECTOR_EMBEDDING` with `MULTILINGUAL_E5_BASE`; a different model should produce and use its own dimension count.
