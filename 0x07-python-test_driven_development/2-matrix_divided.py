#!/bin/usr/python3
"""
this module is to divide each element of matrix by a number of int/float
"""


def is_matrix(matrix):
    """test if a element is a matrix"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        return False
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            return False
    return True


def matrix_divided(matrix, div):
    """
    return a matrix with each element of row divided by div
    each element is rounded by 2

    """
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if (not is_matrix(matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if (is_matrix(matrix)):
        value = True
        for row in matrix:
            if (len(row) != len(matrix[0])):
                value = False
        if (not value):
            raise TypeError(
                "Each row of the matrix must have the same size"
                )
    matrix_mod = []
    for row in matrix:
        row_mod = []
        for element in row:
            row_mod.append(round(element / div, 2))
        matrix_mod.append(row_mod)
    return matrix_mod
