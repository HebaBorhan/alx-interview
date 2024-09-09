#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates 2D matrix 90 degrees clockwise in-place"""
    # Transpose matrix
    matrix[:] = [list(row) for row in zip(*matrix)]

    # Reverse each row for clockwise rotation
    matrix[:] = [row[::-1] for row in matrix]
