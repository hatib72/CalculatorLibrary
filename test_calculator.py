"""
Unit tests for the calculator library
"""


from calculator import add, subtract, multiply, divide


class TestCalculator:
    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        assert 100 == multiply(10, 10)

    def test_division(self):
        assert 4 == divide(20, 5)
