"""
In this example we have tried to use _only_ property tests with hypothesis
to reach the solution.

We start by eliminating negative numbers from the strategies. Note that for the
consecutive terms test we have to start at n=2 to avoid calling fib on a negative
number.
"""

from hypothesis import given, strategies

from project_euler.problem_2 import fibonacci, fibonacci_sequence


class TestPropertyFibonacci:
    @given(strategies.integers(min_value=1, max_value=100))
    def test_returns_integer(self, n: int):
        assert type(fibonacci(n)) == int

    @given(strategies.integers(min_value=2, max_value=100))
    def test_consecutive_terms(self, n: int):
        assert (fibonacci(n - 2) + fibonacci(n - 1)) == fibonacci(n)


class TestPropertyFibonnaciSequence:
    @given(strategies.integers(min_value=1, max_value=100))
    def test_returns_sequence_of_integer(self, n: int):
        for result in fibonacci_sequence(n):
            assert type(result) == int

    @given(
        strategies.integers(min_value=3, max_value=100),
        strategies.integers(min_value=0, max_value=97),
    )
    def test_sequence_is_fib(self, n_terms: int, look_at: int):
        # we have to make sure look_at isn't too large
        look_at = min(n_terms - 3, look_at)
        # turn the iterator to a list for easier indexing
        result = list(fibonacci_sequence(n_terms))

        assert result[look_at] + result[look_at + 1] == result[look_at + 2]
