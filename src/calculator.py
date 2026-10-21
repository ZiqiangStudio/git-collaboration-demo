"""计算器核心业务模块，供协作演练使用。"""
import math

def add(a: float, b: float) -> float:
    """两数求和。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """两数相减。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """两数相乘。"""
    return a * b


def divide(a: float, b: float) -> float:
    """两数相除。"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base: float, exponent: float) -> float:
    """计算底数的指数幂。"""
    if base == 0 and exponent < 0:
        raise ValueError("零不能作为负指数的底数")
    return base**exponent





def is_prime(n):
    # 边界处理：n < 2 返回 False
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("输入必须是整数")

    if n < 2:
        return False

    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 试除法，只检查到 √n，跳过偶数
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True
