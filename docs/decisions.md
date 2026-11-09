# S02 implementation decisions and open items

The authoritative cross-service decision log is in the [portfolio repository](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/decisions/decision-log.md). This document records implementation-specific choices without overriding it.

- Verified: standalone FastAPI and Open WebUI Workspace Tool paths are both MVP acceptance scenarios.
- Verified: Workspace Tool adapter bridges chat attachments to FastAPI multipart upload; direct OpenAPI upload failed HTTP 422.
- Approved architecture unchanged: Python 3.11.5, modular FastAPI, Open WebUI, Podman development, deterministic findings and hosted-model explanation.
- Verified: original source and tests are in GitHub; optional association forwarding passed automated tests and a user-reported live synthetic three-file workflow. The Workspace Tool returns report text rather than a user-downloadable ZIP.
- Pending or deferred: reproducible deployment, user-accessible ZIP if required, SEC-001 design and verification.
- Shared-core review: S02 is the first verified service milestone. **Defer extraction** until genuine cross-service reuse is demonstrated; revisit with the owner at each subsequent solution milestone.

## SDR-001 — Portfolio MVP scope versus commercial readiness (2026-11-06)

**Decision:** Complete a compact synthetic-data-only Variant 1 mini-software portfolio MVP, then build and compare a ChatGPT Skill-based Variant 2 using shared synthetic datasets and acceptance criteria. Do not require production hardening or every conceivable CRM rule to declare the portfolio MVP complete.

**Context and rationale:** The objective is to demonstrate business problem framing, deterministic audit logic, API and AI integration, regression testing and engineering judgment. Implementing full commercial controls now would increase effort without improving that core portfolio demonstration proportionally.

**Consequences and trade-offs:** The MVP cannot process real customer CRM data or claim production readiness. Deferred security, privacy, operational, data-source completeness, and commercial requirements remain visible in the [commercial readiness backlog](commercial-readiness-backlog.md), not forgotten or implicitly waived. The [definition of done](definition-of-done.md) remains the MVP acceptance gate.

**Portfolio presentation:** A [business-facing S02 case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) is maintained in the portfolio repository, linking back to technical evidence here. The case study records the completed and closed synthetic-data portfolio MVP and the accepted two-variant comparison.
