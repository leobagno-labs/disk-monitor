# Disk Monitor

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

```ini
[pytest]
pythonpath = .
