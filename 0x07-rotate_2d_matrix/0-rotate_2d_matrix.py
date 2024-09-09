#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place"""
    # Transpose the matrix
    matrix[:] = [list(row) for row in zip(*matrix)]

    # Reverse each row to get the clockwise rotation
    matrix[:] = [row[::-1] for row in matrix]
