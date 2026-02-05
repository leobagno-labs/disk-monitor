# Disk Monitor

![Profile Views](https://komarev.com/ghpvc/?username=leobagno-labs&color=blue&style=flat)
![Tests](https://img.shields.io/badge/tests-6%20passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A small Python project focused on defensive system metrics logic
and unit testing.

## Version 1 Scope

Version 1 focuses on core business logic and tests.

Included in v1:

- Metrics helpers (`clamp`, `used_percent`, unit conversions)
- Defensive handling of edge cases (zero values, negatives, boundaries)
- Formatting helpers
- Unit tests using pytest
- Test configuration via `pytest.ini`

Out of scope for v1:

- Docker / containerization
- Packaging for distribution (PyPI)
- Prometheus / Grafana integration
- OS-specific collectors

## Testing

Tests are written using `pytest`.  

Import resolution is handled via `pytest.ini`, which adds the repository root to Python's module search path.

To run the tests, execute:

```bash
pytest -v tests/test_metrics.py
```

Expected output:

```tests/test_metrics.py::test_clamp PASSED
tests/test_metrics.py::test_used_percent PASSED
tests/test_metrics.py::test_bytes_to_gib PASSED
tests/test_metrics.py::test_diskstats_immutable PASSED
tests/test_metrics.py::test_format_disk_summary PASSED
tests/test_metrics.py::test_format_memory_summary PASSED

====== 6 passed in 0.XX s ======
```
