#!/usr/bin/python3
"""
this module is to print a square which size given argument

"""


def print_square(size):
    """print a square with given size"""
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        ligne = "#" * size
        print(ligne)

