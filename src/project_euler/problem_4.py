import itertools
from typing import Generator


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def products(min: int, max: int) -> Generator[int, None, None]:
    return (x * y for x, y in itertools.product(range(min, max), range(min, max)))


def solve(n_digits) -> int:
    min_number = 10 ** (n_digits - 1)
    max_number = 10**n_digits

    return max(x for x in products(min_number, max_number) if is_palindrome(x))


if __name__ == "__main__":
    print(solve(3))
