# Commercial readiness backlog — beyond the portfolio MVP

**Status:** Deferred planning backlog; not implemented or verified unless evidence is recorded elsewhere.  
**Scope:** S02 Variant 1, the Python/FastAPI and Open WebUI CRM auditor. The current portfolio MVP is **synthetic-data-only**, not production-ready.

This document is the canonical inventory of work deliberately omitted from the portfolio MVP. It is **not** a promise that every item is necessary for every customer: deployment model, contractual obligations, CRM source system, data sensitivity, and customer acceptance criteria determine the final commercial scope.

## Release gates before real customer CRM data

| Area | Commercial work to scope and verify | Acceptance evidence required |
| --- | --- | --- |
| SEC-001 and data handling | Implement sensitivity classification, explicit approval where required, and fail-closed controls; determine whether any data or report content can reach a hosted AI provider. | Approved data-flow/threat review; automated negative tests; approval and blocking evidence |
| Privacy and compliance | Determine controller/processor roles, lawful processing basis, retention/deletion, subprocessor and data-residency requirements, and relevant contractual/privacy obligations (including GDPR where applicable). | Reviewed customer-specific data-processing and compliance documentation; verified retention/deletion behavior |
| Authentication and authorization | Restrict API, uploads, reports and Open WebUI tool access to authorized users; assess tenant isolation if multiple customers are supported. | Access-control and isolation tests, including unauthorized attempts |
| Secrets, transport and storage | Manage credentials securely, encrypt network traffic and sensitive stored artifacts as appropriate, minimize persistence, and prevent leaks through logs or model context. | Configuration review, secret scanning, transport/storage checks and deletion tests |
| Input and failure security | Harden CSV parsing, schema and file-size validation, resource limits, error handling, abuse controls and dependency security. | Malformed/adversarial input tests, dependency review and failure-path evidence |
| Operational deployment | Make setup reproducible across supported environments; define configuration, upgrades, backups if applicable, recovery and rollback. | Fresh-environment installation, Podman/network smoke tests and recovery exercise |
| Observability and support | Add appropriate health checks, audit-safe logs, monitoring, alerting, incident response and support ownership. | Operational runbook and demonstrated incident/failure handling |
| Reliability and capacity | Establish supported file sizes, response times, concurrency limits, timeout behavior and recovery from partial failures. | Load/performance and resilience results against agreed targets |
| Release quality | Establish reproducible dependency installation, CI regression checks, versioning, change review and vulnerability management. | Passing automated pipeline, release record and documented maintenance process |
| Business acceptance | Agree on business rules, false-positive handling, severity, owner policy, sample exports and customer sign-off criteria. | Signed-off rule catalogue and customer-specific acceptance tests |

## Business-rule and source-data expansion (conditional on the commercial offer)

| Area | Deferred work | Dependency / decision |
| --- | --- | --- |
| Complete association coverage | Distinguish full exports from partial reference lists before claiming missing deal-contact links. | CRM export completeness and association semantics |
| Freshness checks | Obtain reliable extraction/update timestamps, time zone and freshness thresholds. | Source metadata and customer-defined SLA |
| Close-date reconciliation | Compare source values and transformations under an approved rule. | Original close dates and documented CRM policy |
| Pipeline and deal-quality rules | Extend stage, amount, owner and required-field rules to actual customer workflows. | Agreed stage catalogue and owner/field policies |
| Contact identity and deduplication | Validate normalization, matching thresholds, acceptable duplicates and false positives. | CRM identity and deduplication policy |
| Data completeness and integrity | Add source-specific relationships, record coverage and schema-drift handling. | Reliable exports, field mappings and completeness evidence |
| Explainability and report governance | Validate severity, evidence, coverage disclaimers and AI explanations against deterministic results; prevent unsupported claims. | Representative approved scenarios and human review |
| Integration and automation | Evaluate native CRM connectors, scheduled runs, notifications and remediation only if commercially required. | Customer workflow and least-privilege permissions |

## Commercial delivery and market validation

- Validate buyer need, target users, packaging, pricing and support expectations.
- Define service-level commitments, onboarding, documentation, training and change management.
- Run an authorized, controlled pilot **only after** the applicable security and privacy gates are met.
- Obtain customer acceptance and clarify liability, contract and operational ownership before production rollout.
- Revisit shared-core extraction only after actual reuse across services is demonstrated and approved.

## Relationship to existing documents

- [Definition of done](definition-of-done.md) owns **Portfolio MVP acceptance** and per-change verification; this backlog does not enlarge the MVP gate.
- [Security](security.md) owns the current SEC-001 status and security architecture limitations.
- [Deployment](deployment.md) owns deployment instructions and verified environment status.
- [Service specification](service-specification.md) owns current business scope and supported inputs/outputs.
- [Validation](validation.md) owns executed test evidence, not planned tests.
- [Project status](../PROJECT-STATUS.md) owns the current milestone and next tiny action.

**Rule:** Do not mark an item complete based solely on code presence or a plan. Record actual test evidence and customer-specific acceptance where applicable. Never process real customer CRM data in the current synthetic-only MVP.
