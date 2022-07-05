#!/usr/bin/python3
"""advanced task"""

def add_attribute(obj, name, value):
    if "__dict__" not in dir(type(obj)):
        raise TypeError("can't add new attribute")
    obj.setattr(name, value)
