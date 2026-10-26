# S02 validation record

Status: Verified synthetic-data integration milestone; evidence reported from development tests, not rerun from this repository.

| Scenario | Result | Scope |
| --- | --- | --- |
| Standalone FastAPI audit | Passed | Synthetic CRM CSVs, ZIP output |
| Open WebUI attachment metadata | Passed | Two attachments with readable paths |
| Workspace Tool multipart upload | Passed | FastAPI HTTP 200 and ZIP response |
| Conversational audit explanation | Passed | Model described deterministic findings |
| Direct OpenAPI `/audit` upload | Failed | HTTP 422 missing multipart files |
| SEC-001 enforcement | Not implemented | No customer-data clearance |

Observed synthetic results: **202 contacts**, **121 deals**, **92 medium findings**, all `CRM-DEAL-OWNER-MISSING`. ZIP report includes `summary.json`, `issues.csv`, `report.md`. Contact associations, close-date source reconciliation and freshness checks were not fully evaluated due to incomplete source data. Rules remain provisional pending CRM owner-policy review.

Next: import actual FastAPI source, dependencies and test fixtures, rerun reproducible local tests, test invalid/missing inputs and optional associations, and verify container portability.
