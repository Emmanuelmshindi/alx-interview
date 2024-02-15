#!/usr/bin/python3
"""Prime game interview question"""
def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            return True

    def winner(n):
        if n == 1:
            return "Ben"
        elif n == 2:
            return "Maria"
        elif isPrime(n):
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if winner(n) == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if maria_wins < ben_wins:
        return "Ben"
    else:
        return None
