#!/usr/bin/python3
"""
Solves the N queens puzzle using backtracking.
"""

import sys

def nqueens(N):
    def is_safe(board, row, col):
        """Check if it's safe to place a queen at board[row][col]."""
        # Check the left side of the row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower left diagonal
        for i, j in zip(range(row, N), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nqueens_util(board, col):
        """Recursively solve the N Queens puzzle."""
        if col >= N:
            solutions.append([row[:] for row in board])
            return

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve_nqueens_util(board, col + 1)
                board[i][col] = 0

    if not N.isdigit():
        print("N must be a number")
        return

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        return

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens_util(board, 0)

    for solution in solutions:
        print(solution)
