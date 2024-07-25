#!/usr/bin/python3
"""Pascal"""


def pascal_triangle(n):
    """Pascal"""
    if n <= 0:
        return []

    pascalTriangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j])
        row.append(1)
        pascalTriangle.append(row)

    return pascalTriangle
