# content of test_class.py
import pytest
from calculator import Calculator


class TestCalculator:

    def test_add(self):
        calc = Calculator(10, 5)
        assert calc.add() == 15

    def test_subtract(self):
        calc = Calculator(10, 5)
        assert calc.subtract() == 5

    def test_multiply(self):
        calc = Calculator(10, 5)
        assert calc.multiply() == 50

    def test_multiply(self):
        calc = Calculator(10, 5)
        assert calc.multiply() == 50

    def test_divide_by_zero(self):
        calc = Calculator(10, 0)
        with pytest.raises(ZeroDivisionError):
            calc.divide()

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -2, -3),
        (2.5, 3.5, 6.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.add() == expected