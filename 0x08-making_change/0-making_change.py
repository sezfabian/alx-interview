#!/usr/bin/python3
"""Making change module
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins
    needed to meet a given total
    """
    i = 0
    numberOfCoins = 0

    coins.sort(reverse=True)

    if total == 0 or total < 0:
        return 0

    while total > 0:
        if total / coins[i] > 0:
            numberOfCoins += int(total / coins[i])
            total = total % coins[i]

        i += 1

        if i == len(coins) and total > 0:
            return -1

    return numberOfCoins
