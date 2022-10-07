"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import truediv

def primes(number_of_primes):
    list = []
    num = 0
    while len(list) < number_of_primes:
        if isPrime(num):
            list.append(num)
        num += 1
    return list

def isPrime(num):
    flag = True
    if num <= 1:
        flag = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag
