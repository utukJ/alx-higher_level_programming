#!/usr/bin/python3
"""inherits from int"""


class MyInt(int):
    """inherits from int and reverses equality"""
    
    def __eq__(self, other):
        return not super().__eq__(other)
