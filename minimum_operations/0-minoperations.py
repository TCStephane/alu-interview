#!/usr/bin/python3
"""Module that computes the minimum operations to reach n characters."""


def minOperations(n):
    """Return the fewest operations (Copy All, Paste) to get n 'H' chars.

    The answer is the sum of the prime factors of n.
    Return 0 if n is impossible to achieve (n < 2 or not an integer).
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
