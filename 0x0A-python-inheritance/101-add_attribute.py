#!/usr/bin/python3
"""advanced task"""

def add_attribute(obj, name, value):
    """adds new attribute or raises TypeError if unable"""
    if "__dict__" not in dir(type(obj)):
        raise TypeError("can't add new attribute")
    obj.setattr(name, value)
