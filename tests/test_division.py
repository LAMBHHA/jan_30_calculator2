"""
Tests the add() function of the calculator.
"""
from calculator import division


def test_ten_divided_by_two():
    """
    If given 10 and 2 as parameters, 5 should
    be returned
    """
    assert division(10, 2) == 5

def test_nine_divided_by_three():
    assert division(9, 3) == 3
    """
    If given 9 and 3 as parameters, 3 should
    be returned
    """

def test_no_parameter():
    """ if no parameters are provided, return 0
    """
