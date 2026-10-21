import pytest
from src.calculator import add, divide, multiply, power, subtract, is_prime

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




def test_is_prime():
    # 典型质数
    assert is_prime(2) is True
    assert is_prime(13) is True
    assert is_prime(97) is True

    # 合数
    assert is_prime(4) is False
    assert is_prime(100) is False

    # 边界值
    assert is_prime(-5) is False
    assert is_prime(0) is False
    assert is_prime(1) is False

    # 非法输入抛异常
    with pytest.raises(TypeError):
        is_prime(3.14)
