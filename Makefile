.PHONY: test lint format

test:
	uv run pytest tests/

lint:
	uv run pre-commit run --all-files

format:
	uv run ruff --fix .
