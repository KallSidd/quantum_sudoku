"""
Unit and regression test for the quantum_sudoku package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import quantum_sudoku


def test_quantum_sudoku_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "quantum_sudoku" in sys.modules
