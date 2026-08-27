# Source Traceability

## Source Register

| Source | Classification | Evidence Used | Workshop Areas | Treatment |
| --- | --- | --- | --- | --- |
| [Search Examples using Oracle AI Database API for MongoDB](https://blogs.oracle.com/autonomous-ai-database/search-examples-using-oracle-ai-database-api-for-mongodb) | Oracle-owned public source | Search concepts, model and index commands, MongoDB aggregation examples, movie-search workflow | Introduction and Labs 1–3 | Summarized and adapted into tasks |
| [Using Oracle Database API for MongoDB](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/mongo-using-oracle-database-api-mongodb.html) | Oracle-owned public documentation | Schema-to-database mapping, collection-to-table mapping, learner-user requirements, and `mongosh` connection pattern | Introduction, workshop environment contract, and Lab 1 | Summarized and adapted |
| [JSON, MongoDB API, and Duality Views Workshop](https://github.com/oracle-livelabs/database/tree/main/json-mongo-duality-general) | Oracle-owned public workshop | General LiveLabs onboarding structure and four OCI/MongoDB API screenshots | Get Started variants and sandbox screenshots | Structure was reviewed; screenshots were copied into this Oracle-owned workshop with task-specific filenames |
| [MongoDB Shell Download](https://www.mongodb.com/try/download/shell) | External product download page | Current MongoDB Shell version and official download location | Get Started | Linked for software download only; no instructional content copied |
| [JSON Collections](https://docs.oracle.com/en/database/oracle/oracle-database/26/adjsn/json-collections.html) | Oracle-owned public documentation | Oracle 26ai JSON collection table shape and `DATA` column | Lab 1 and Lab 2 SQL | Used for technical validation |
| [DBMS_CLOUD for Objects and Files](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/dbmscloud-for-objects-and-files.html) | Oracle-owned public documentation | `COPY_COLLECTION` behavior and parameters | Lab 1 | Adapted to the supplied movie dataset URL |
| [LOAD_ONNX_MODEL_CLOUD](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/load_onnx_model_cloud.html) | Oracle-owned public documentation | ONNX model loading behavior and parameters | Lab 1 | Cross-checked against the source blog command |
| [ORDS_ADMIN.SET_PROPERTY](https://docs.oracle.com/en/database/oracle-rest-data-services/25.3/orddg/oracle-rest-data-services-administration-pl-sql-package-reference.html) | Oracle-owned public documentation | Non-schema ORDS property syntax and administrator access | Tenancy Get Started | Used to validate the `mongo.preview` property task |
| [MovieStream movie JSON objects](https://objectstorage.us-ashburn-1.oraclecloud.com/n/c4u04/b/moviestream_landing/o/movie/*.json) | Oracle-hosted public dataset | Sample collection loaded at runtime | Lab 1 | Referenced directly; not copied into the workshop repository |
| Workshop design requirements supplied by the workshop owner | Oracle internal design input | SQL sandbox, `mongosh`, dual-interface checkpoints, and embedding checkpoint | Workshop outline and Lab 1 | Converted into learner outcomes and environment requirements |

## Asset Register

- The Get Started lab includes three Oracle-owned screenshots from the JSON, MongoDB API, and Duality Views Workshop:
  - `get-started/images/open-database-actions.png`
  - `get-started/images/copy-mongodb-api-url.png`
  - `get-started/images/open-cloud-shell.png`
- Both Get Started variants include `get-started/images/navigate-to-autonomous-ai-database.png` and `get-started-tenancy/images/navigate-to-autonomous-ai-database.png`, user-supplied Oracle Cloud Console screenshots. The workshop owner confirmed their use for this build.
- Both Get Started variants include `open-object-storage-buckets.png`, a user-supplied Oracle Cloud Console screenshot that shows how to open Object Storage buckets. The workshop owner confirmed its use for this build.
- The tenancy Get Started variant includes `get-started-tenancy/images/open-cloud-shell.png`, a user-supplied Oracle Cloud Console screenshot that shows how to open Cloud Shell. The workshop owner confirmed its use for this build.
- The tenancy Get Started variant includes `get-started-tenancy/images/copy-mongodb-api-url.png`, a user-supplied Oracle Cloud Console screenshot that shows the MongoDB API access URL. The workshop owner confirmed its use for this build.
- The source screenshots show sample or redacted environments only. They contain no learner sandbox credentials.
- The `MOVIES` dataset is loaded at runtime from the Oracle-hosted public Object Storage URL.
- The ONNX model binary is not bundled. The publishing team must supply the provided multilingual E5-base model URL in the sandbox environment.

## Scope Notes

- The clickable Oracle blog URL supplied in the request is the controlling source. The link label named a different article.
- The workshop now combines the Oracle blog workflow with the workshop owner's explicit sandbox and Lab 1 requirements.
- Oracle documentation was used to validate collection loading, MongoDB API connectivity, and ONNX model loading.
- The requested output folder uses capitalization supplied by the workshop owner. Internal lab folders and files retain lowercase LiveLabs naming.
