#!/usr/bin/python3
"""
Minimum operation
"""


def minOperations(n):
    """ This method calculates the fewest number of operations needed
    to result in exactly n H characters in the file. """
    if n == 1:
        return 0

    # Initialize an array to store the minimum operations for each number
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 H requires 0 operations

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                # If j is a divisor of i, then we can achieve i
                # by copying j times and pasting
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0  # If impossible, return 0
