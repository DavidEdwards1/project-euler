"""
The implmentation of `fibonacci_recursive` is in fact _tree recursive_ growing rapidly
in both time and space complexity with n.

The function `fibonacci` is a linear iterative process. It should scale linearly
in time complexity and then have constant space complexity.

The function `fibonacci_generator` takes the idea of `fibonacci_linear` and
instead `yield`s each value. Internally  `fibonacci_sequence`uses this approach
to avoid recalculating the same numbers.
"""

from typing import Generator, Iterator


def fibonacci_recursive(n: int) -> int:
    if n == 0:
        ans = 1
    elif n == 1:
        ans = 1
    else:
        ans = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return ans


def fibonacci(n: int) -> int:
    a, b = 1, 1
    for i in range(n):
        a, b = b, b + a
    return a


def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        a, b = b, b + a
        yield a


def fibonacci_sequence(n_terms: int) -> Generator[int, None, None]:
    gen = fibonacci_generator()
    return (next(gen) for i in range(n_terms))


def fibonacci_sequence_until(max_value: int) -> Generator[int, None, None]:
    gen = fibonacci_generator()
    while (value := next(gen)) < max_value:
        yield value


def is_even(x: int) -> bool:
    return x % 2 == 0


def solve(max_value: int) -> int:
    return sum(n for n in fibonacci_sequence_until(max_value) if is_even(n))


if __name__ == "__main__":
    print(solve(4_000_000))
