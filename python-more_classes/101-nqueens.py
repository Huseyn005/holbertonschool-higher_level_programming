#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(board, row + 1, n)
            board.pop()


solve_nqueens([], 0, n)
