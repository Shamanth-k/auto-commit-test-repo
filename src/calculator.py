"""Calculator utilities."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


DIVISION_BY_ZERO_MESSAGE = "Cannot divide by zero"


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError(DIVISION_BY_ZERO_MESSAGE)
    return a / b


def power(base: float, exponent: float) -> float:
    return base ** exponent


def absolute(value: float) -> float:
    return abs(value)


def percentage(value: float, percent: float) -> float:
    return value * percent / 100