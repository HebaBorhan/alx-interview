#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    # Grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    # Traverse each cell in grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # if there is land above
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1

                # if there is land below
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1

                # if there is land to left
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1

                # if there is land to right
                if c < cols - 1 and grid[r][c+1] == 1:
                    perimeter -= 1

    return perimeter
