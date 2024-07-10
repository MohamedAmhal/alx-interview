#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 20
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

def run_tests():
    test_cases = [
        # Minimum Input
        (1, 0),
        
        # Small Prime Numbers
        (3, 3),
        
        # Perfect Squares
        (4, 4),
        
        # Composite Numbers
        (6, 5),
        (9, 6),
        (12, 7),
        
        # Larger Prime Numbers
        (13, 13),
        
        # Larger Composite Numbers
        (18, 8),
        (20, 9),
        (24, 10),
        (27, 9),
        (28, 11),
        (30, 10),
        
        # Impossible Case
        (0, 0),
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        result = minOperations(n)
        assert result == expected, f"Test case {i + 1} failed: minOperations({n}) = {result}, expected {expected}"
        print(f"Test case {i + 1} passed")


if __name__ == "__main__":
    run_tests()
