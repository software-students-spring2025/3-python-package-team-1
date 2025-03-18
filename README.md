![Python build & test](https://github.com/nyu-software-engineering/python-package-example/actions/workflows/build.yaml/badge.svg)

# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Project Structure

```
RatPack/
├── src/
│   └── ratpack/
│       ├── __init__.py          # Package initialization and imports
│       └── infest.py            # Core functionality implementation
│
├── tests/
│   ├── __init__.py              # Test package initialization
│   ├── conftest.py              # Test fixtures and utilities
│   ├── test_infest_decorator.py # Tests for @infest decorator
│   ├── test_count_rats.py       # Tests for count_rats function
│   ├── test_exterminate.py      # Tests for exterminate function
│   ├── test_visualize_infestation.py # Tests for visualize_infestation function
│   └── test_integration.py      # Integration tests
│
├── .github/
│   └── workflows/               # GitHub Actions workflows
│
├── README.md                    # Project documentation
├── LICENSE                      # Project license
├── Pipfile                      # Project dependencies
└── setup.py                     # Package configuration for distribution
```

This structure follows Python best practices with a clear separation between source code and tests. The package is designed to be easily installable, testable, and maintainable.
