#!/usr/bin/python3
"""
Main file for code !
"""


from typing import List


def divisions(n) -> List[int]:
    '''
    this function is return the divisions of the number n
    we have one para,eter n
    '''
    return [i for i in range(2, n + 1) if (n % i == 0)]


def minimum(l: List[int]) -> int:
    '''
    this function is return the minimum of a list
    that containt the sum of the decomposion of a number n
    '''
    min = l[0]
    for i in l:
        if i <= min:
            min = i

    return min


def minOperations(n) -> int:
    '''
    this function return the min operations to create the H n time
    we have also one parameter n
    '''
    if (n <= 1):
        return 0
    elif (n == 2 or n == 3):
        return n
    else:
        lilo = divisions(n)
        vector = []
        for i in lilo:
            if i != n:
                vector.append(int(i + (n / i)))
            else:
                vector.append(int(n))
        return minimum(vector)
