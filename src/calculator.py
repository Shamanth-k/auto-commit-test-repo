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
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return value * percent / 100


def square(value: float) -> float:
    return value * value


def percentage_fraction(percent: float) -> float:
    return percent / 100


def reciprocal(value: float) -> float:
    if value == 0:
        raise ValueError(
            "Cannot calculate reciprocal of zero"
        )
    return 1 / value


def minimum(values: list[float]) -> float:
    if not values:
        raise ValueError(
            "values cannot be empty"
        )
    return min(values)
