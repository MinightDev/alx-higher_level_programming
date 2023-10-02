#!/usr/bin/python3
"""
N-Queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions.
"""

import sys

def nqueens(N):
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

    def solve(board, col):
        if col == N:
            solutions.append(board[:])
            return
        for row in range(N):
            if is_safe(board, row, col):
                board[col] = row
                solve(board, col + 1)

    if not isinstance(N, int) or N < 4:
        print("N must be a number and at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve(board, 0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
