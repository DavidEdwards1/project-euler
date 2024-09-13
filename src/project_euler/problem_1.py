"""
The interesting thing here is that we end up with two functions that should
potentially be one: `is_multiple_of` and `is_multiple_ofs` where the second
takes a tuple instead of the single value accepted by the first. Ideally, we would
have a generic n-tuple version of the function but that seems like overkill for
the simple cases. The recursive option is interesting, and leads to some specific
questions:
 - does Python's or short-circuit?
 - will it short-circuit in a recurisve function or will it try and resolve the
   recursive calls first?
"""


def is_multiple_of(n: int, x: int):
    return x % n == 0


def is_multiple_ofs(ns: tuple[int, int], x):
    return is_multiple_of(ns[0], x) or is_multiple_of(ns[1], x)


def solve(max_n: int) -> int:
    return sum(n for n in range(1, max_n) if is_multiple_ofs((3, 5), n))


if __name__ == "__main__":
    print(solve(1000))
