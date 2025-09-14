# Python Template

A minimal Python project template demonstrating best practices for packaging, testing, and linting.

## Project Overview

- Source code lives in the `src/` directory.
- Tests are located in the `tests/` directory.
- Build configuration is defined in `pyproject.toml`.
- Development utilities (linting, formatting) are available via the `Makefile`.

## Prerequisites

* Python ≥ 3.12
* [`uv`](https://github.com/astral-sh/uv) for dependency management

## Setup

```bash
# Install dependencies
uv sync
```

The command reads the `[project]` section of `pyproject.toml` and installs the required packages.

## Running the code

There is no dedicated entry‑point script, but you can experiment with the example module:

```bash
# Run an interactive session
uv run python -c "from src.arithm import sum; print(sum(2, 3))"
```

## Testing

Run all tests:

```bash
make test
```

Or invoke pytest directly:

```bash
uv run pytest tests/
```

## Linting & Formatting

```bash
# Run pre‑commit hooks (lint, type checking, etc.)
make lint

# Auto‑format code with ruff
make format
```

## Project Structure

- `src/` – source modules
- `tests/` – test suite
- `Makefile` – convenient shortcuts for common tasks
- `pyproject.toml` – project metadata and dependencies
- `.pre-commit-config.yaml` – pre‑commit hook configuration

## License

This project is licensed under the terms found in the [LICENSE](LICENSE) file.
