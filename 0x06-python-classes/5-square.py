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
        self.size = size

    @property
    def size(self):
        """
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        sets size of square to val

        Args:
            val (int): new size of the square, must be greater than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            Area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        Prints square using '#'
        """
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("\n", end="")
