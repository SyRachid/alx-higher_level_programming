#!/usr/bin/python3
"""This module help to define a class of Square."""


class Square:
    """The class that define a Square."""
    def __init__(self, size=0):
        """constructor of  my class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method that return the area of the square"""
        return self.__size**2
