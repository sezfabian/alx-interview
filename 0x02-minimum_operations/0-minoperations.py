#!/usr/bin/python3
"""
Module 0-minoperations
"""


def minOperations(n: int) -> int:
    """
    Return the  fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations: int = 0
    for i in range(min_operations, n + 1):
        while n % i == 0:
            n = n / i
            operations += i
    return operations
