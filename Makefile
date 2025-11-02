.PHONY: test lint format

test:
	uv run --exact --package arithm pytest packages/arithm
	uv run --exact --package example-cli pytest packages/example-cli

lint:
	uv run pre-commit run --all-files

format:
	uv run ruff --fix .
