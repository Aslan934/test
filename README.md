# Dummy Project

A minimal dummy Python project scaffold.

## Structure

- `src/dummy_project/` — package source code
- `tests/` — pytest tests
- `pyproject.toml` — project metadata and dependencies

## Run

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv/bin/activate   # or .venv\Scripts\activate on Windows
   ```
2. Install dependencies:
   ```bash
   python -m pip install -U pip
   python -m pip install .
   ```
3. Run the package:
   ```bash
   python -m dummy_project
   ```
4. Run tests:
   ```bash
   python -m pytest
   ```
