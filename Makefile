# Makefile
.PHONY: test
test:
	poetry run pytest tests/

.PHONY: linting
linting:
	poetry run isort src
	poetry run black --line-length 120 src
	poetry run flake8 --ignore=E226,E302,E41,W191,W503 --max-complexity=13 --max-line-length=120 src

.PHONY: mypy
mypy:
	poetry run mypy src

.PHONY: run
run:
	poetry run py src/cross_stitch_tasks/api/run.py