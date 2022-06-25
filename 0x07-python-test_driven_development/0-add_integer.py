#!/usr/bin/python3
"""Add integers"""


def add_integer(a, b=98):
    """
    Given two integers, return the sum

    Args:
        a (int): first integer in sum
        b (int): second integer in sum (default 98)

    Returns:
        int: sum of a and b
    """
    allowed_param_types = (int, float)
    if type(a) not in allowed_param_types:
        raise TypeError("a must be an integer")
    if type(b) not in allowed_param_types:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
