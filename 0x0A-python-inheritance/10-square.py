#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defines a Square"""
    def __init__(self, size):
        """construtor method"""
        self.__size = size
        super().__init__(self.__size, self.__size)
