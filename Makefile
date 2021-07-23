#
# RunParser Makefile
# Just helps manage repetitive/tedious commnands
#
# (C) 2021 Andrew Augustine
#

# first, variables

py := python3
venv_dir := .venv
venv_script := $(venv_dir)/bin/activate
venv_cmd := source $(venv_script)

# now, target definitions

.ONESHELL:

help:
	@echo "Available targets are: init, test, build, venv, help"

init:
	@if [ -d "$(venv_dir)" ]; then echo "Project already setup!"; exit 1; fi
	$(py) -m venv $(venv_dir)
	$(venv_dir)/bin/$(py) -m pip install -r requirements.txt

test:
	@echo "Running tests..."
	$(py) -m unittest -v tests

build: test
	@echo "Building package..."
	$(py) -m pip install --upgrade build
	$(py) -m build

venv:
	@echo ""
	@echo "Subprocesses cannot source files for you lol"
	@echo "Run '$(venv_cmd)' to get venv to work"
	@echo ""
	exit 1

.PHONY: help init test build venv
.DEFAULT: help