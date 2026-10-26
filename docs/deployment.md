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

**Repository gap:** the original FastAPI source and dependency manifest are not yet available in this GitHub repository. Transfer them from the working local project; do not infer or regenerate business logic from these notes. Deployment instructions are not independently reproducible until that transfer and a fresh smoke test.
