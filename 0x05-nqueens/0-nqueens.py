#!/usr/bin/python3
"""
Determines all possible solutions to N Queens problem, where N queens
are placed on an N×N chessboard such that no two queens threaten each other.
"""

import sys


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen
    at the given row and column on the board.
    """
    # Check this column on the upper side
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    """
    Solves N Queens problem and returns all possible solutions.
    """
    def solve(board, row):
        if row == N:
            # If all queens are placed, add the solution
            solutions.append([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
