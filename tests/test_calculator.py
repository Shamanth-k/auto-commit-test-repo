import pytest

from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)   

def test_divide_by_zero():
    import pytest

    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_multiply_negative_numbers():
    assert multiply(-5, -3) == 15
