from math import prod
from hypothesis import given, strategies
import pytest

from project_euler.problem_3 import is_prime, prime_factors, solve


class TestPropertyIsPrime:
    @given(strategies.integers(min_value=2))
    def test_returns_bool(self, n: int):
        assert type(is_prime(n)) == bool

    @given(strategies.integers(min_value=2))
    def test_even_numbers_are_not_prime(self, n: int):
        assert is_prime(2 * n) == False


class TestUnitIsPrime:
    @pytest.mark.parametrize("n", [3, 5, 7, 11, 13, 17, 19, 23, 29])
    def test_known_primes_are_prime(self, n):
        assert is_prime(n) == True


class TestPropertyPrimeFactors:
    @given(strategies.integers(min_value=2, max_value=600_851_475_143))
    def test_product_of_factors_is_input(self, n: int):
        assert prod(prime_factors(n)) == n

    @given(strategies.integers(min_value=2, max_value=600_851_475_143))
    def test_list_of_factors_all_prime(self, n: int):
        assert all(is_prime(x) for x in prime_factors(n))


class TestUnitListPrimeFactors:
    @pytest.mark.parametrize("n, factors", [(3, [3]), (13195, [5, 7, 13, 29])])
    def test_known_factors(self, n: int, factors: list[int]):
        assert list(prime_factors(n)) == factors


class TestUnitSolve:
    @pytest.mark.parametrize("n,largest_factor", [(13195, 29)])
    def test_known_result(self, n: int, largest_factor: int):
        assert solve(n) == largest_factor
