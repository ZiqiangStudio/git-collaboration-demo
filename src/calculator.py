"""计算器核心业务模块，供协作演练使用。"""


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
