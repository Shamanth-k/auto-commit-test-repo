"""Calculator utilities."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
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


def calculate(
    operation: str,
    a: float,
    b: float,
) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        raise ValueError(
            f"Unsupported operation: {operation}"
        )

    return operations[operation](a, b)


def round_value(value: float, digits: int = 2) -> float:
    return round(value, digits)
