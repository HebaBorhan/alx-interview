#!/usr/bin/python3
"""Min Operations"""


def minOperations(n):
    """Return the minimum number of operations to result n H characters in text file"""
    if n <= 1:
        return 0
    
    numberOperations = 0
    primeFactor = 2
    
    while n > 1:
        while n % primeFactor == 0:
            numberOperations += primeFactor
            n = n // primeFactor
        primeFactor += 1
    
    return numberOperations
