base_python := python3
py := poetry run

reports_dir := reports


# =================================================================================================
# Environment
# =================================================================================================

.PHONY: install
install:
	$(base_python) -m pip install --user -U poetry
	poetry install

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -name .pytest_cache`
	rm -rf *.egg-info
	rm -f .coverage
	rm -f report.html
	rm -f .coverage.*
	rm -rf {build,dist,site,.cache,.mypy_cache,reports}

# =================================================================================================
# Code quality
# =================================================================================================

.PHONY: isort
isort:
	$(py) isort -rc vkwave tests

.PHONY: black
black:
	$(py) black vkwave tests

.PHONY: mypy
mypy:
	$(py) mypy vkwave

.PHONY: mypy-report
mypy-report:
	$(py) mypy vkwave --html-report $(reports_dir)/typechecking

.PHONY: lint
lint: isort black mypy

# =================================================================================================
# Tests
# =================================================================================================

.PHONY: test
test:
	$(py) pytest tests/

.PHONY: test-coverage
test-coverage:
	mkdir -p $(reports_dir)/tests/
	$(py) pytest --html=$(reports_dir)/tests/index.html tests/
	$(py) coverage html -d $(reports_dir)/coverage

# =================================================================================================
# Docs
# =================================================================================================

.PHONY: docs
docs:
	$(py) mkdocs build

.PHONY: docs-serve
docs-serve:
	$(py) mkdocs serve

.PHONY: docs-copy-reports
docs-copy-reports:
	mv $(reports_dir)/* site/reports

# =================================================================================================
# Project
# =================================================================================================

.PHONY: build
build: clean mypy-report test-coverage docs docs-copy-reports
	mkdir -p site/simple
	poetry build
	mv dist site/simple/vkwave
