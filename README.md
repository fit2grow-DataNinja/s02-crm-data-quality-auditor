# S02 — CRM Data Quality & Freshness Auditor

AI-assisted CRM data quality and freshness auditing using deterministic Python/FastAPI checks and Open WebUI conversational reporting.

**Status:** Working synthetic-data MVP integration; **not production-ready**. Original FastAPI source and dependencies still need to be imported from the verified local project.

## Navigation
- [Service specification](docs/service-specification.md)
- [Architecture and integration boundaries](docs/architecture.md)
- [Open WebUI adapter and setup](docs/integration.md)
- [Local deployment](docs/deployment.md)
- [Validation evidence](docs/validation.md)
- [Security and SEC-001 limitations](docs/security.md)
- [Service-specific decisions](docs/decisions.md)
- [Open WebUI Workspace Tool source](integrations/openwebui/s02_csv_audit_adapter.py)
- [Portfolio governance and approved architecture](https://github.com/bb-DataNinja/ai-services-portfolio)

**Verified synthetic sample:** 202 contacts, 121 deals, 92 medium missing-deal-owner findings. The conversational adapter returns the report text, not a downloadable ZIP.

**Security:** SEC-001 sensitivity tagging/manual approval is **not implemented**. Use synthetic data only. Do not upload real customer CRM data to this MVP.

**Source transfer required:** This repository currently contains the adapter and documentation, **not** the existing local FastAPI application, tests or dependency manifest. Copy those from the working local checkout before treating this repository as executable.

**Shared-core checkpoint:** Review potential `ai-services-core` reuse at every verified solution milestone; do not create shared infrastructure without demonstrated reuse and approved change control.
