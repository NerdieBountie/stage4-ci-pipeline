"""
tests/test_calculator.py – Full test suite for the calculator module.
The CI pipeline runs these tests automatically on every push and pull request.
A single failing assertion will cause the entire pipeline to fail.
"""

import pytest
from src.calculator import add, subtract, multiply, divide, power


# ──────────────────────────────────────────────
# add()
# ──────────────────────────────────────────────
class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_mixed_sign(self):
        assert add(-10, 15) == 5

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero_identity(self):
        assert add(99, 0) == 99


# ──────────────────────────────────────────────
# subtract()
# ──────────────────────────────────────────────
class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_result_negative(self):
        assert subtract(3, 7) == -4

    def test_same_values(self):
        assert subtract(5, 5) == 0

    def test_floats(self):
        assert subtract(1.5, 0.5) == pytest.approx(1.0)


# ──────────────────────────────────────────────
# multiply()
# ──────────────────────────────────────────────
class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(999, 0) == 0

    def test_negative(self):
        assert multiply(-3, 4) == -12

    def test_two_negatives(self):
        assert multiply(-3, -4) == 12

    def test_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


# ──────────────────────────────────────────────
# divide()
# ──────────────────────────────────────────────
class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_one(self):
        assert divide(42, 1) == 42

    def test_negative_dividend(self):
        assert divide(-10, 2) == -5.0

    def test_zero_numerator(self):
        assert divide(0, 5) == 0.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


# ──────────────────────────────────────────────
# power()
# ──────────────────────────────────────────────
class TestPower:
    def test_basic(self):
        assert power(2, 10) == 1024

    def test_zero_exponent(self):
        assert power(999, 0) == 1

    def test_one_exponent(self):
        assert power(7, 1) == 7

    def test_fractional_exponent(self):
        assert power(9, 0.5) == pytest.approx(3.0)

    def test_negative_base(self):
        assert power(-2, 3) == -8
