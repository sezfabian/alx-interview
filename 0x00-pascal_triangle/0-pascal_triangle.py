#!/usr/bin/python3
"""
Module defines function for pascal Triangle
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle
    """
    Myarray = []

    if n <= 0:
        return Myarray

    Myarray.append([1])

    if n == 1:
        return Myarray

    row = [1, 1]
    Myarray.append(row)

    for i in range(2, n):
        row = [1] + [Myarray[i-1][j-1]
                     + Myarray[i-1][j] for j in range(1, i)] + [1]
        Myarray.append(row)

    return Myarray
