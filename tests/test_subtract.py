"""
Tests the add() function of the calculator.
"""
from calculator import subtract


def test_five_minus_two():
    """
    If given 5 and 2 as parameters, 3 should
    be returned
    """
    assert subtract(5, 2) == 3

def test_eight_minus_three():
    assert subtract(8, 3) == 5
    """
    If given 8 and 3 as parameters, 5 should
    be returned
    """

def test_no_parameter():
    """ if no parameters are provided, return 0
    """
