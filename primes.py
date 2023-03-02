from math import isqrt
from time import perf_counter

'''Returns a list of Primes less than n
    uses an optimized naive iteration'''


def find_primes(n):
    primes = [2]
    if n < 2:
        return []
    for number in range(3, n, 2):
        isPrime = True
        for divisor in range(3, isqrt(number)+1, 2):
            if number % divisor == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)

    return primes


def isPrime(n):

    if n < 2: return False
    if n == 2 or n == 3: return True

    for i in range(3, isqrt(n)+1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':

    start = perf_counter()
    for i in range(1_000_000):
        for y in range(isqrt(i)):
            if i > 0:
                i = i
    print(perf_counter() - start)
