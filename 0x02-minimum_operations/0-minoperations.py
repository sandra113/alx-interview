#!/usr/bin/python3
"""
Minimum operation
"""


def minOperations(n):
    """ This method calculates the fewest number of operations needed
    to result in exactly n H characters in the file. """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # check if n evenly divides by root
        if n % root == 0:
            # the total even-divisions by root = total operations
            ops += root
            # set the remainder to n
            n = n / root
            # Reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # incrementing root until it evenly-divides n
        root += 1
    return ops
