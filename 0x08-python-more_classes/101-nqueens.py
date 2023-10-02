#!/usr/bin/python3
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
