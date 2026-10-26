# Project status — S02 CRM Data Quality & Freshness Auditor

**Last updated:** 2026-10-26  
**Phase:** Working synthetic-data MVP; source-control and reproducibility gap.  
**Status:** Active; **not production-ready**.

## Current working step
**Transfer the existing, verified local FastAPI application source, dependency manifest and tests from the Mac to this repository.** The GitHub repository currently contains documentation and the Open WebUI Workspace Tool adapter, but **not** the original FastAPI implementation.

### Next tiny action
**Identify the working local S02 project folder and list its files**, so we can choose exactly what to commit without copying the virtual environment, credentials, customer data or generated ZIPs. Do not recreate source code from documentation.

### Last completed
- Merged S02 repository foundation and Open WebUI adapter into `main` (commit `bc34183`).
- Merged related portfolio registry, documentation governance and shared-core checkpoint into portfolio `main` (commit `8a78290`).
- Confirmed standalone FastAPI and Open WebUI Workspace Tool conversational audit paths with synthetic data.
- Documented security and integration limitations in `docs/`.

## Verified evidence (historical local tests; not rerun from GitHub)
- Local FastAPI: `GET /health`; `POST /audit` accepts required `contacts`, `deals` and optional `associations` multipart fields; returns ZIP containing `summary.json`, `issues.csv`, `report.md`.
- Synthetic inputs: 202 contacts and 121 deals; 92 medium findings of type `CRM-DEAL-OWNER-MISSING`.
- Open WebUI Workspace Tool adapter successfully forwards `contacts.csv` and `deals.csv` to the local API and returns deterministic summary and report text.
- Direct OpenAPI External Tool Server `/audit` from chat failed HTTP 422 due to missing multipart attachments. `/health` working does not validate file upload.
- Optional associations are not supported by the current Workspace Tool adapter; freshness and reconciliation coverage remain incomplete.

## Implementation plan / checkpoints
| Checkpoint | State | Next evidence |
| --- | --- | --- |
| S02 repository docs, adapter and portfolio links | Complete | Merged to `main` |
| Original FastAPI source and dependency manifest | **Current** | Transfer verified local files without secrets or generated artifacts |
| Source-controlled tests and fixtures | Pending | Import original tests or add explicitly reviewed synthetic tests |
| Fresh checkout standalone audit | Pending | Run health, multipart audit and inspect ZIP |
| Fresh checkout Open WebUI chat audit | Pending | Attach two synthetic CSVs; verify tool result and model explanation |
| Optional associations and freshness coverage | Pending | Agree rules and test representative fixtures |
| SEC-001 sensitivity/manual approval enforcement | **Not implemented** | Design, approval, negative tests and fail-closed verification |
| Portable deployment and operational checks | Pending | Reproduce on documented Podman environment |
| Customer/commercial validation | Pending | Separate from technical acceptance |

## Decisions and constraints
- Both standalone FastAPI and Open WebUI conversational workflows are required MVP scenarios.
- Keep deterministic audit rules authoritative; hosted AI may explain results but should not invent findings.
- **Synthetic data only:** hosted model can receive tool output, and SEC-001 outbound-data controls are not implemented.
- Do not change approved architecture v0.1, create `ai-services-core`, or alter repositories beyond agreed scope without owner approval.
- Shared-core checkpoint at each verified solution milestone: review common functions, integration utilities, tests and documentation; record whether to defer, reference or propose extraction. Initial S02 outcome: **defer extraction until reuse is demonstrated**.

## Resume instructions for a new chat
1. Read this file and the [portfolio status](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/PROJECT-STATUS.md).
2. Confirm the working tree/repository state before changes.
3. Continue from **Next tiny action**, one small step at a time.
4. At the end of each meaningful step, update this file and recommend a GitHub commit if files changed.

## Reference documents
- [Service specification](docs/service-specification.md)
- [Integration instructions](docs/integration.md)
- [Validation evidence](docs/validation.md)
- [Security limitations](docs/security.md)
- [Portfolio architecture baseline](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/architecture/baseline-v0.1.md)
