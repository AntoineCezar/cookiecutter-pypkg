.PHONY: help test typecheck clean clean-test clean-pyc clean-build
.DEFAULT_GOAL := help

PACKAGE_NAME = {{ cookiecutter.package_name }}

VIRTUALENV ?= python -m venv
VIRTUAL_ENV ?= .venv
PYTHON ?= $(VIRTUAL_ENV)/bin/python
PIP ?= $(VIRTUAL_ENV)/bin/pip
BROWSER ?= firefox

define PRINT_HELP_PYSCRIPT
import re, sys

data = []
target = ''
help = []
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):', line)
	if match and target and help:
		data.append((target, help))
	if match:
		target = match.group(1)
		help = []
		continue

	match = re.match(r'^\t+@## *(.+) *', line)
	if match:
		help.append(match.group(1))

if target and help:
	data.append((target, help))
col_widht = max([len(t) for t, h in data])
template = "  %-{}s  %s".format(col_widht)

for target, help in data:
	print(template % (target, help[0]))
	for line in help[1:]:
		print(template % ('', line))
	print('')
endef
export PRINT_HELP_PYSCRIPT


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

$(PYTHON):
	$(VIRTUALENV) $(VIRTUAL_ENV)
	$(PIP) install "setuptools >= 30.3.0"

develop: $(PYTHON)
	@## install the package in develop mode
	$(PIP) install -e ".[testing]"
	$(PIP) install -e ".[develop]"
	$(PIP) install -e .

test:
	@## run tests quickly with the default Python
	$(PYTHON) -m unittest

typecheck:
	@## check types with mypy
	$(PYTHON) -m mypy $(PACKAGE_NAME)

lint:
	@## check style with flake8
	$(PYTHON) -m flake8 $(PACKAGE_NAME) tests

coverage:
	@## show coverage in the console
	$(PYTHON) -m coverage run -m unittest
	$(PYTHON) -m coverage report -m

coverage-html:
	@## show coverage in the browser
	@## uses $BROWSER if present
	$(PYTHON) -m coverage run -m unittest
	$(PYTHON) -m coverage html
	$(BROWSER) htmlcov/index.html

dist: clean
	@## build source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

clean: clean-build clean-pyc clean-test
	@## remove all build, test, coverage and Python artifacts

clean-build:
	@## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	@## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
