#!/usr/bin/python3
"""
Given n number of locked boxes.
Each box numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

This module defines a method that
determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    """
    unlocked = [1] + [0] * (len(boxes) - 1)
    if len(boxes) == 1:
        return True

    for key in boxes[0]:
        if key == 0:
            continue
        if key < len(boxes) and unlocked[key] == 0:
            unlocked[key] = 1
            unlocked = unlockBox(boxes, key, unlocked)

    if unlocked == [1] * len(boxes):
        return True
    return False


def unlockBox(boxes, key, unlocked):
    """
    Unlock a box.
    """
    for newkey in boxes[key]:
        if newkey < len(boxes) and unlocked[newkey] == 0:
            unlocked[newkey] = 1
            unlocked = unlockBox(boxes, newkey, unlocked)

    return unlocked
