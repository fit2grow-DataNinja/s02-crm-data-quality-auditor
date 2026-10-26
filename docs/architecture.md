# S02 implementation architecture

Status: Observed MVP integration; not a replacement for portfolio architecture v0.1.

The approved platform baseline and architecture change policy live in the [portfolio repository](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/architecture/baseline-v0.1.md).

## Verified paths
1. Standalone: local FastAPI `POST /audit` accepts multipart CRM CSV exports, invokes deterministic checks, and returns a ZIP report.
2. Conversational: Open WebUI chat receives CSV attachments; a Workspace Tool reads attachment paths, submits multipart data to FastAPI at `http://host.containers.internal:8000/audit`, reads `summary.json` and `report.md` from ZIP, and returns findings for hosted-model explanation.
3. `GET /health` works from the Open WebUI external OpenAPI integration.

The external OpenAPI `/audit` tool did **not** successfully forward chat attachments (HTTP 422 for missing multipart fields); the Workspace Tool adapter is the validated conversational path. The original OpenAPI tool should not be presented as the working upload path.

## Boundaries
Deterministic Python/SQL rules own findings; the model handles routing and explanation. Open WebUI's hosted-model orchestration does not demonstrate the planned backend outbound-data policy gate. Do not assume client-sensitive content is safe to transmit. See [security](security.md).

The portfolio approved one modular FastAPI application initially; this separate source repository is an ownership boundary, **not** authorization to deploy a new independent application or infrastructure component.
