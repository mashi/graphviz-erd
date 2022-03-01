SHELL := /bin/bash

hello:
	echo "hello world"

install:
	(\
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip install wheel; \
		pip install -r requirements.txt; \
		pip install -r docs/requirements-docs.txt; \
		pre-commit install; \
	)

docs:
	(\
		source .venv/bin/activate; \
		sphinx-build -E -b html docs/source docs/_build; \
	)

# to always execute a recipe: use FORCE
# https://www.gnu.org/software/make/manual/html_node/Force-Targets.html
tests: FORCE
	(\
		source .venv/bin/activate; \
		python -m unittest discover -b; \
	)

FORCE:
