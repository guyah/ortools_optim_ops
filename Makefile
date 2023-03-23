install:
	pip install --upgrade pip
	pip install -r requirements.txt


install_dev:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	# Installs the pre-commit hook.
	pre-commit install
