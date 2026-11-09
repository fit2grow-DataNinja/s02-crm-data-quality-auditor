# S02 security status

Status: **SEC-001 planned, not implemented or tested**.

The [portfolio security baseline](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/architecture/baseline-v0.1.md) requires sensitivity tagging, fail-closed handling and manual approval for applicable sensitive-data operations. This control is not operational in S02.

The Open WebUI adapter reads attached CSV bytes and sends them to the local FastAPI host. It then returns the deterministic summary and Markdown report into the chat tool context, which may be processed by the configured hosted AI model. Do not use real customer or sensitive CRM data in this configuration. Synthetic datasets only until an approved backend policy gate and appropriate security review are implemented and verified.

No claims of GDPR compliance, tenant isolation, authorization, EU processing guarantees or production readiness are supported by current tests. Do not commit credentials, customer exports, private reports or generated archives.
