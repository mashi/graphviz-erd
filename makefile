# Note that, to always execute a recipe, it is recommended [1] to use the FORCE prerequisite
# [1] https://www.gnu.org/software/make/manual/html_node/Force-Targets.html

SHELL := /bin/bash

hello:
	echo "hello world"

# install all the required packages and configure the git hooks
install:
	(\
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip install wheel; \
		pip install -r requirements.txt; \
		pip install -r docs/requirements-docs.txt; \
		pre-commit install; \
	)

# build the documentation with sphinx
docs:
	(\
		source .venv/bin/activate; \
		sphinx-build -E -b html docs/source docs/_build; \
	)

# execute tests
tests: FORCE
	(\
		source .venv/bin/activate; \
		python -m unittest discover -b; \
	)

# build the python package for pypi.org
build: FORCE
	(\
		source .venv/bin/activate; \
		python -m build; \
	)

FORCE:
