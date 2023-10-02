#!/usr/bin/python3i
"""
This program uses backtracking to find and print the coordinates of N queens on an NxN grid,
ensuring that they are all in non-attacking positions.
"""


import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position on the board.
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    """
    Solve the N Queens problem using backtracking.
    """
    def backtrack(board, col):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(board, col + 1)

    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])

