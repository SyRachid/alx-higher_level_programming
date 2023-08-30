#!/usr/bin/python3
"""This module help to define a class of Square."""


class Square:
    """The class that define a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """constructor of  my class"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position attribut"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
                print(" " * self.__position[0] + "#" * self.__size)
