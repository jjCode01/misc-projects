import math
import timeit
from functools import partial


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    limit = int(math.sqrt(num))

    for i in range(2, limit + 1):
        if num % i == 0:
            return False

    return True


def all_primes2(num: int) -> list[int]:
    if num <= 1:
        return []

    if num == 2:
        return [2]

    primes: list[int] = [2]

    for n in range(3, num + 1):
        limit: int = int(math.sqrt(n))

        for prime in primes:
            if prime > limit:
                primes.append(n)
                break
            if n % prime == 0:
                break

    return primes


def all_primes(num: int) -> list[int]:
    if num <= 1:
        return []

    if num == 2:
        return [2]

    primes: list[bool] = [False, False] + [True] * (num - 1)
    limit = int(math.sqrt(num))

    for n in range(limit + 1):
        if primes[n] is False:
            continue

        mult = n
        while (product := n * mult) <= num:
            primes[product] = False
            mult += 1

    return [i for i, n in enumerate(primes) if n is True]


if __name__ == "__main__":
    partial_function = partial(all_primes, num=10000)
    execution_time = timeit.timeit(partial_function, number=100)
    print("Execution time:", execution_time)

    partial_function2 = partial(all_primes2, num=10000)
    execution_time2 = timeit.timeit(partial_function2, number=100)
    print("Execution time 2:", execution_time2)
