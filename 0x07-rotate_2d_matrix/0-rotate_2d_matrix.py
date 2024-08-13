#!/usr/bin/python3
'''
documentations
documentations
doc doc doc doc doc doc !
@mohammedamhal
'''


def transpose(matrix, n):
    '''
    transpose a matrix 2d
    n * n size !!!
    '''
    for i in range(n):
        for j in range(n):
            if i != j and i > j:
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a


def rotate_2d_matrix(matrix):
    '''
    the function that relate the matrix
    of the size n * n!
    '''
    n = len(matrix)
    transpose(matrix, n)
    print(matrix)
    for i in range(n):
        for j in range(n):
            if j <= (n / 2 - 1):
                a = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = a
