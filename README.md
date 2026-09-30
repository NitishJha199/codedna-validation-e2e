# CodeDNA Validation E2E

Purpose-built repository for validating CodeDNA automated GitHub evidence ingestion.

Services:
- order-api
- inventory-api

The order-api intentionally contains a controlled historical urllib3 dependency
for validating security correlation and service-level blast radius.
