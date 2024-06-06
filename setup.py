from setuptools import setup, find_packages

setup(
    name="domain_inspector",
    version="0.1.0",
    author="Kody Gaston",
    author_email="kody.gaston@msn.com",
    description="A tool to fetch and analyzes domain information",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kagaston/domain_inspector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "whois",
        "pendulum",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "mypy",
            "black",
            "isort",
            "bandit",
            "pre-commit",
        ],
    },
    entry_points={
        'console_scripts': [
            'domain_inspector=domain_inspector.__main__:main',
        ],
    },
)
