import pytest
from src.calculator import add, divide, multiply, power, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3
    assert power(2, 0) == 1
    with pytest.raises(ValueError, match="零不能作为负指数的底数"):
        power(0, -2)
