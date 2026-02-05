"""Check that basic features work.

Catch cases where e.g. files are missing so the import doesn't work. It is
recommended to check that e.g. assets are included."""

# tests/smoke_test.py
import sys

import water_bottle_please  # replace with your actual package name
from water_bottle_please import helpers

def test_basic_import():
    """Check that the package can be imported."""
    assert water_bottle_please is not None

def test_basic_functionality():
    """Optionally check one key function."""
    result = helpers.date_format(col="test")
    assert result is not None

if __name__ == "__main__":
    test_basic_import()
    test_basic_functionality()
    print("Smoke test passed!")

