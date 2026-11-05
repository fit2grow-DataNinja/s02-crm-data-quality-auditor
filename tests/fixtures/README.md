# Regression test fixtures

This directory is reserved for **small, reusable, synthetic-only** test inputs and expected outputs.

## Rules
- Keep scenario-specific data inline or generate it in a temporary directory when that is simpler. The existing `tests/test_openwebui_adapter.py` follows this approach and needs no copied fixture.
- Add a named fixture here only when it is reused by multiple tests or is important as a stable regression example.
- Keep any expected outputs alongside their inputs with descriptive names; assert relevant fields rather than unstable formatting.
- Never commit real CRM/customer exports, credentials, personal information, or generated reports containing sensitive data.
- Keep existing larger demonstration datasets under `samples/`; do not duplicate them here.
- Each bug fix or behavior change should add or update a regression test that fails for the defect and passes after the fix.

Run the test suite from the repository root with:

```bash
python -m unittest discover -s tests -v
```

See [Definition of done](../../docs/definition-of-done.md) for acceptance criteria.
