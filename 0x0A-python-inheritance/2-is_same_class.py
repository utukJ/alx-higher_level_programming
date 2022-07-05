#!/usr/bin/python3
"""Task 2"""


def is_same_class(obj, a_class):
    """returns bool indicating if obj is exact instance of a_class"""
    return type(obj) == type(a_class)
