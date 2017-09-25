.PHONY: help test typecheck clean clean-test clean-pyc clean-build
.DEFAULT_GOAL := help

PACKAGE_NAME = {{ cookiecutter.package_name }}

VIRTUALENV ?= python -m venv
VIRTUAL_ENV ?= .venv
PYTHON ?= $(VIRTUAL_ENV)/bin/python
PIP ?= $(VIRTUAL_ENV)/bin/pip
BROWSER ?= firefox


help:
	@echo -e "Usage:\n"
	@awk ' \
		/^[a-zA-Z_-]+:/ { \
			t = $$0; \
			sub(/:.*/, "", t) \
		} \
		/^\s+@?##/ { \
			h = $$0; \
			sub(/^\s*@*##/, "", h); \
			print "\t" t "\t" h; \
			t = "" \
		} \
		' Makefile | column -t -s $$'\t'


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
	$(PYTHON) -m coverage run -m unittest
	$(PYTHON) -m coverage html
	$(BROWSER) htmlcov/index.html

dist: clean
	@## builds source and wheel package
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
	@## remove coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
