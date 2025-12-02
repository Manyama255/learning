### Project snapshot

- Single-file Python project: `main.py` (prints "hello world").
- No dependency files (no requirements.txt, no pyproject.toml).
- No tests or CI configuration detected.

### What an AI coding agent should know (big picture)

- The repository is intentionally minimal — it's a single Python script at the repo root (`main.py`). Keep changes focused and small unless the user asks to expand the project.
- There are no service boundaries, packages, or integrations to respect. Treat additions as new files rather than modifying unrelated code.

### Common developer workflows & how to run things locally

- To run the project locally use the user's shell (bash) with a Python 3 interpreter:

```bash
python main.py
```

- There are no automated tests or linters. If you add tests, prefer `pytest` in a `tests/` directory and commit test requirements in `requirements.txt`.

### Conventions and patterns observed

- File layout is flat. New code should be added in logical folders (for example `src/`, `tests/`, or `docs/`) when the project grows — do not restructure the repository without an explicit user request.
- Keep function names and modules small and well-scoped. For an initial feature, prefer adding a new module (e.g. `src/my_feature.py`) and a test file (`tests/test_my_feature.py`).

### What to avoid

- Don't introduce large or opinionated frameworks (Django/Flask/FastAPI) without user agreement — the repo currently shows no sign of frameworks.
- Avoid changing global project structure when adding example code (keep single-purpose files and small tests nearby).

### Good first actions for an AI agent

- Confirm the runtime by running `python main.py` and show the output string `hello world` back in your change summary.
- If expanding functionality, add `requirements.txt` and a `tests/` folder with `pytest` to demonstrate CI-friendly changes.

### Example edits that follow the repo's current footprint

- Add a new module `src/utils.py` that contains small, focused functions and a `tests/test_utils.py` file to validate behavior.
- Keep commit messages concise and focused: `feat: add utils.format_message()` / `test: add tests for utils.format_message()`.

If anything here is unclear or you want the file to cover a different scope, tell me where to focus (e.g., expanding into a library or adding CI). 
