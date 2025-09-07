# Data Fetcher

**Data Fetcher** is a Python library to fetch and process JSON data from public APIs.  
It includes:

- A **retry decorator** for reliable API calls.
- Functions to **filter** and **extract fields** from JSON data.
- Fully typed, tested, and formatted for professional use.

---

## Features

- Fetch JSON data with automatic retries on failure.
- Filter lists of dictionaries by key/value pairs.
- Extract specific fields from JSON responses.
- Fully typed with **mypy**, formatted with **Black**, and linted with **Flake8**.
- Includes **Pytest** tests and CI/CD ready GitHub Actions workflow.

---

## Installation

```powershell
# Clone the repository
git clone https://github.com/ansonne/data-fetcher.git
cd data-fetcher

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
.\.venv\Scripts\activate.bat # Windows CMD
# or
source .venv/bin/activate      # Linux / macOS

# Install the package in editable mode
pip install -e .

# Install development dependencies
pip install pytest black flake8 mypy types-requests
```

---

## Testing

```powershell
## Run all tests
pytest -v

## Run type checks
python -m mypy src

## Run code formatting check
black --check src tests

## Run linter
flake8 src tests
```

---

## License

MIT License © 2025 André Luiz. See the LICENSE file for details.
