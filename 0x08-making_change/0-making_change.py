#!/usr/bin/python3
"""fewest number of coins"""


def makeChange(coins, total):
    """determine the fewest number of coins,
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity for all totals except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Fill dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[total] infinity, impossible to form total
    return dp[total] if dp[total] != float('inf') else -1
