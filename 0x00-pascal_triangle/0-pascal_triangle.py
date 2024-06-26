#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Pascal's Triangle is a triangular array where each entry is the sum of the 
    two entries directly above it. This function returns a list of lists, where 
    each inner list represents a row of Pascal's Triangle. If n is less than or 
    equal to 0, the function returns an empty list.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists representing Pascal's Triangle up to n rows.

    Examples:
    >>> pascal_triangle(5)
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    >>> pascal_triangle(3)
    [
        [1],
        [1, 1],
        [1, 2, 1]
    ]

    >>> pascal_triangle(0)
    []

    >>> pascal_triangle(-1)
    []

    ====>MOHAMMED <====
    """
    liste = []
    a = [1]
    b = [1, 1]

    # check the n number:
    if (n <= 0) :
        return (liste)
    
    else :
        liste.append(a)
        liste.append(b)
        for i in range(2, n):
            a = []
            a.append(1)
            for j in range(1, i):
                a.append(b[j] + b[j - 1])
            a.append(1)
            liste.append(a)
            b = a
        
        return (liste)




            

