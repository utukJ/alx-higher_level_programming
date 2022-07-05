#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defines a Square"""
    def __init__(self, size):
        """construtor method"""
        super().__init__(size, size)
        self.__size = size
