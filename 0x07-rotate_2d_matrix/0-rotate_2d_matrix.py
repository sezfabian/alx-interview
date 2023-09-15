#!/usr/bin/python3
"""0. Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):
    """Rotate 2D matrix"""
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()

    return matrix        
