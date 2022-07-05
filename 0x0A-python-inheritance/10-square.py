#!/usr/bin/python3
"""
more class base
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """ definition of a Rectangle """
    def __init__(self, width, height):
        """ constructor and width, height"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


class Square(BaseGeometry):
    """defines a Square"""
    def __init__(self, size):
        """construtor method"""
        self.__size = size
        BaseGeometry.integer_validator(self, "size")

    def area(self):
        return self.__size ** 2