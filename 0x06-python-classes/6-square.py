#!/usr/bin/python3
"""
This module implements a square class
"""


class Square:
    """Square class with input validation"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size (int): size of the square, must be greater than 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Args:
            position (tuple): size 2 tuple representing position of the square
        """
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Returns:
            Area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        prints square using '#'
        """
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size, end="\n")
