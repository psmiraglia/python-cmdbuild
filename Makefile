SOURCES := setup.py \
	cmdbuild/__init__.py \
	cmdbuild/cmdbuild.py \
	cmdbuild/cards/__init__.py \
	cmdbuild/cards/base.py \
	cmdbuild/cards/network_interface.py

default: install

install:
	pip install -e .

flake8:
	flake8 $(SOURCES)

isort-diff:
	isort --diff $(SOURCES)

isort:
	isort $(SOURCES)

style: flake8 isort-diff
