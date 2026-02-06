IMAGE_NAME := project-chimera:dev

.PHONY: setup test spec-check build test-local

build:
	docker build -t $(IMAGE_NAME) .

setup: build
	@echo "Attempting to install dependencies using uv inside container..."
	docker run --rm $(IMAGE_NAME) sh -c "which uv >/dev/null 2>&1 && uv install || pip install -r requirements.txt || true"

test: build
	@echo "Running pytest inside Docker container"
	docker run --rm $(IMAGE_NAME) pytest -q

spec-check:
	python3 scripts/spec_check.py

test-local:
	@echo "Running pytest in local .venv"
	.venv/bin/python -m pytest -q
