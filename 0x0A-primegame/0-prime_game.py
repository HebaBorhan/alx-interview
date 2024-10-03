#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds"""
    if not nums or x < 1:
        return None

    # Determine the maximum value of n we will deal with
    max_n = max(nums)

    # Step 1: Sieve of Eratosthenes to determine prime numbers up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Step 2: Create a list to keep track of the number of primes <= n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Step 3: Simulate the rounds
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 4: Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
