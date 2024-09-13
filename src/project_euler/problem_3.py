from functools import lru_cache
import math
from typing import Generator


@lru_cache
def has_factor(n: int, x: int) -> bool:
    """
    Returns True if x divides n exactly
    """
    return n % x == 0


@lru_cache
def is_prime(n: int) -> bool:
    return not any(has_factor(n, x) for x in range(2, int(math.sqrt(n)) + 1))


def prime_factors(n: int) -> Generator[int, None, None]:
    """
    Returns a list of the prime factors of n.
    """
    number_to_factor = n
    while not is_prime(number_to_factor):
        next_factor = next(
            x
            for x in range(2, int(math.sqrt(n)) + 1)
            if has_factor(number_to_factor, x)
        )
        number_to_factor = number_to_factor // next_factor
        yield next_factor

    yield number_to_factor


def solve(n: int):
    return max(prime_factors(n))


if __name__ == "__main__":
    print(solve(600_851_475_143))
