#!/usr/bin/python3
'''
documentation
documentation
'''

import sys


def backtracking(r, n, col,  posDiag, negDiag, board):
    '''
    documentations
    documentations
    !!!!
    '''

    if r == n:
        res = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    res.append([i, j])
        print(res)
        return

    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = 1

        backtracking(r+1, n, col, posDiag, negDiag, board)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = 0


def Nquee(n: int):
    '''
    documentations
    documentations
    ddd
    '''
    col = set()  # les colonnes verticaux et horizontaux
    posDiag = set()  # pour les diagonales positives (r + c) est const
    negDiag = set()  # pour les diagonales negatives (r -c) est const
    board = [[0] * n for i in range(n)]

    backtracking(0, n, col, posDiag, negDiag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n1 = int(n[1])
        if n1 < 4:
            print("N must be at least 4")
            sys.exit(1)
        Nquee(n1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
