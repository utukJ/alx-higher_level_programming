#!/usr/bin/python3
"""
This module implements a square class
"""


class Square:
    """Square class with input validation"""

    def __init__(self, size=0):
        """
        Args:
        size (int): size of the square, must be greater than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
