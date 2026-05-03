# Stage 4 – CI/CD Pipeline Project

![CI Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)

A Python calculator module with a full automated test suite wired to GitHub Actions CI. Every push and pull request triggers the pipeline automatically — no manual intervention required.

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI configuration
├── src/
│   ├── __init__.py
│   └── calculator.py       # Application source code
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Full test suite (24 tests)
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Running Locally

### Prerequisites

- Python 3.11+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full test suite
pytest tests/ -v

# 4. Run tests and generate JUnit XML report
pytest tests/ --junitxml=report.xml -v
```

You should see all 24 tests pass with output similar to:

```
tests/test_calculator.py::TestAdd::test_positive_numbers PASSED
tests/test_calculator.py::TestAdd::test_negative_numbers PASSED
...
24 passed in 0.12s
```

---

## CI Pipeline

### Platform

**GitHub Actions** — configuration lives at `.github/workflows/ci.yml`

### Triggers

| Event | Branches |
|-------|----------|
| `push` | all branches |
| `pull_request` | all branches |

### Pipeline Steps

1. **Checkout** – clones the repository at the current commit
2. **Set up Python 3.11** – installs a clean Python runtime
3. **Install dependencies** – runs `pip install -r requirements.txt`
4. **Run tests** – executes `pytest tests/ --junitxml=report.xml -v`
5. **Upload artifact** – saves `report.xml` so results are downloadable from the Actions UI (runs even on failure)

### Failure Behaviour

If **any test fails**, pytest exits with a non-zero code and GitHub Actions marks the job ❌ **failed**. The run is never silently skipped or suppressed. The JUnit XML report is always uploaded so the failure is inspectable.

---

## Environment Variables

This project has no required environment variables. If you extend it to connect to external services (e.g. a database or API), add the relevant secrets in **GitHub → Settings → Secrets and variables → Actions** and reference them in `ci.yml` as `${{ secrets.YOUR_SECRET }}`.

---

## Test Coverage

| Module | Tests |
|--------|-------|
| `add()` | 5 |
| `subtract()` | 4 |
| `multiply()` | 5 |
| `divide()` | 6 |
| `power()` | 5 |
| **Total** | **25** |

---

## License

MIT
