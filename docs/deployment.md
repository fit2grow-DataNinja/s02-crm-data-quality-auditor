# Local development and deployment notes

Status: Development-machine setup verified; portable deployment untested.

## Standalone API
From the **existing local S02 source checkout** with its dependencies installed:

```bash
source .venv/bin/activate
python -m uvicorn s02.api:app --host 127.0.0.1 --port 8000
```

Verify `http://127.0.0.1:8000/health` and inspect `http://127.0.0.1:8000/docs`. `/audit` expects multipart form fields `contacts`, `deals`, and optionally `associations`.

## Open WebUI
The verified development setup used Podman and Open WebUI at `http://localhost:3000`; the Workspace Adapter calls the host API using `host.containers.internal:8000`. Network reachability depends on the local Podman configuration and must be rechecked after migration.

**Portability gap:** FastAPI source, dependency manifests and tests are version-controlled in this repository. A fresh-environment installation, independent deployment smoke test and portable Podman configuration remain unverified; do not claim reproducible deployment yet.
