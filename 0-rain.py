#!/usr/bin/python3
"""Module for calculating rainwater retained between walls."""


def rain(walls):
    """Calculate how much rainwater is retained between walls.

    Args:
        walls: list of non-negative integers representing wall heights,
            each wall having a width of 1.

    Returns:
        Integer total of square units of water retained after it rains.
        Returns 0 if the list is empty.
    """
    if not walls:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    total = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                total += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                total += right_max - walls[right]
            right -= 1

    return total
