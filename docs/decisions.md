# S02 implementation decisions and open items

The authoritative cross-service decision log is in the [portfolio repository](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/decisions/decision-log.md). This document records implementation-specific choices without overriding it.

- Verified: standalone FastAPI and Open WebUI Workspace Tool paths are both MVP acceptance scenarios.
- Verified: Workspace Tool adapter bridges chat attachments to FastAPI multipart upload; direct OpenAPI upload failed HTTP 422.
- Approved architecture unchanged: Python 3.11.5, modular FastAPI, Open WebUI, Podman development, deterministic findings and hosted-model explanation.
- Pending: transfer original source and tests, optional associations support, user-accessible ZIP, reproducible deployment, SEC-001 design and verification.
- Shared-core review: S02 is the first verified service milestone. **Defer extraction** until genuine cross-service reuse is demonstrated; revisit with the owner at each subsequent solution milestone.
