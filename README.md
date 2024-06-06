# Domain Inspector

![Build Status](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg) | 
[![Tests](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=test)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Atest) | 
[![Flake8](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=flake8)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Aflake8) | 
[![Black](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=black)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Ablack) | 
[![Isort](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=isort)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Aisort) | 
[![Mypy](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=mypy)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Amypy) | 
[![Bandit](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml/badge.svg?event=push&job=bandit)](https://github.com/kagaston/domain_inspector/actions/workflows/ci.yml?query=job%3Abandit) 

![Python Version](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10|%203.11-blue)

## Overview

This project is designed to fetch and analyze domain information. It includes configurations for code formatting, linting, type checking, security scanning, and testing to ensure high code quality and maintainability.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/kagaston/domain_inspector.git
    cd domain_inspector
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install .
    ```

4. **Install development dependencies** (if you are setting up a development environment):
    ```bash
    pip install .[dev]
    ```

5. **Install pre-commit hooks**:
    ```bash
    pre-commit install
    ```

## Configuration

The project uses several configuration files to manage different tools and settings:

- **`.env`**: Environment variables configuration.
- **`.flake8`**: Flake8 linter configuration.
- **`mypy.ini`**: Mypy type checker configuration.
- **`bandit.yaml`**: Bandit security linter configuration.
- **`pyproject.toml`**: Central configuration file for build system and tools like Black, isort, mypy, flake8, and Gitleaks.

### .env

Example of the `.env` file:
```plaintext
DATABASE_URL=sqlite:///my_database.db
SECRET_KEY=supersecretkey
DEBUG=True
```

## Usage
To use the domain_inspector, follow this example:
```python
from domain_inspector.core import DomainService

# Example usage
domain_service = DomainService()
domains = ["example.com", "block.xyz"]
domain_info_list = domain_service.fetch_domain_info(domains)
for domain_info in domain_info_list:
    print(domain_info)
```

## Contributing

To contribute to this project, please submit a pull request.

## License

This project is licensed under the MIT License.