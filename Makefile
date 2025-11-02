.PHONY: test lint format run

test:
	uv run --exact --package arithm pytest packages/arithm
	uv run --exact --package example-cli pytest packages/example-cli
	uv run --exact --package webservice pytest packages/webservice

lint:
	uv run pre-commit run --all-files

format:
	uv run ruff --fix .

run:
	uv run --exact --package webservice uvicorn webservice.health:app --host 0.0.0.0 --port 8000
