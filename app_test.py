import pytest
from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 4) == 4

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
