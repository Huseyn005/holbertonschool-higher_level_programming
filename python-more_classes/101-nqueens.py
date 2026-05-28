#!/usr/bin/python3
"""N Queens puzzle solver using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve(board, row, n, solutions):
    """Backtrack to find all solutions."""
    if row == n:
        solutions.append([[r, c] for r, c in board])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append((row, col))
            solve(board, row + 1, n, solutions)
            board.pop()


def nqueens(n):
    """Find and print all N Queens solutions."""
    solutions = []
    solve([], 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
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

    nqueens(N)
