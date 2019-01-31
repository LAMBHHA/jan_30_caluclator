"""
Tests the add() function of the calculator.
"""
from calculator import subtract


def test_five_minus_two():
    """
    If given 2 and 2 as parameters, 4 should
    be returned
    """
    assert subtract(5, 2) == 3

def test_eight_minus_three():
    assert subtract(8, 3) == 5

def test_no_parameter():
    """ if no parameters are provided, return 0
    """
