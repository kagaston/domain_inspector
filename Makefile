.PHONY: all install-dev test flake8 black isort mypy bandit format

OS := $(shell uname)
PACKAGE_MANAGER := $(shell which apt-get || which dnf || echo "none")

all: install-dev test flake8 black isort mypy bandit

install-dev: install-tools
	python -m pip install --upgrade pip setuptools wheel
	poetry install

install-tools:
ifeq ($(OS), Darwin)  # macOS
	@echo "Detected macOS"
	xcode-select --install || true
	brew install gcc || true
else ifeq ($(PACKAGE_MANAGER), /usr/bin/apt-get)  # Debian-based Linux
	@echo "Detected Debian-based Linux"
	sudo apt-get update
	sudo apt-get install -y build-essential
else ifeq ($(PACKAGE_MANAGER), /usr/bin/dnf)  # Red Hat-based Linux
	@echo "Detected Red Hat-based Linux"
	sudo dnf update
	sudo dnf groupinstall -y "Development Tools"
endif

test:
	pytest -vv --junitxml=reports/junit.xml --cov=domain_inspector --cov-report=xml:reports/coverage.xml

flake8:
	flake8 .

black:
	black --check .

isort:
	isort . --check-only

mypy:
	mypy .

bandit:
	bandit -r domain_inspector

format: format-black format-isort

format-black:
	black .

format-isort:
	isort .
