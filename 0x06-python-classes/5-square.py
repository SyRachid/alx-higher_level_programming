#!/usr/bin/python3
"""This module help to define a class of Square."""


class Square:
    """The class that define a Square."""
    def __init__(self, size=0):
        """constructor of  my class"""
        self.__size = size

    def area(self):
        """Method that return the area of the square"""
        return self.__size**2

    @property
    def size(self):
        """Method that retrive the attribute size of class."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Method that print in stdout a square define by #"""
        if (self.__size == 0):
            print()
        elif type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
