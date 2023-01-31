default: install

install:
	pip install -e .

flake8:
	flake8 setup.py cmdbuild/*.py

isort-diff:
	isort --diff setup.py cmdbuild/*.py

isort:
	isort setup.py cmdbuild/*.py

style: flake8 isort-diff
