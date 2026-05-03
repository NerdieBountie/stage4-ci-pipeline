"""
calculator.py – Simple calculator module used to demonstrate CI pipeline.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a multiplied by b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to exponent."""
    return base ** exponent
