import pytest
from Calculator_KB_v03wtests import Calculator

def test_add():
    calculator = Calculator(5.0, 2.0)
    assert calculator.add() == 7

def test_subtract():
    calculator = Calculator(5.0, 2.0)
    assert calculator.subtract() == 3

def test_multiply():
    calculator = Calculator(5.0, 5.0)
    assert calculator.multiply() == 25

def test_divide():
    calculator = Calculator(10.0, 2.0)
    assert calculator.divide() == 5

def test_nth_root():
    calculator = Calculator(9.0, 2.0)
    assert calculator.nth_root() == 3

def test_reset():
    calculator = Calculator(0.0, 0.0)
    assert calculator.reset_memory() == 0
