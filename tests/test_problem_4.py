from hypothesis import given
from hypothesis import given, strategies as st
import pytest

from project_euler.problem_4 import is_palindrome, solve


class TestUnitIsPalindrome:
    @pytest.mark.parametrize("n", [11, 121, 464, 8990998])
    def test_known_palindromes_are_palindrome(self, n):
        assert is_palindrome(n) == True

    @pytest.mark.parametrize("n", [15, 127, 264, 89930998])
    def test_known_non_palindromes_are_not_palindrome(self, n):
        assert is_palindrome(n) == False


class TestPropertyIsPalindrome:
    @given(st.integers(min_value=0))
    def test_is_palindrome_returns_bool(self, n):
        assert isinstance(is_palindrome(n), bool)


class TestUnitSolve:
    @pytest.mark.parametrize("n", [2])
    def test_solve_gives_known_solution(self, n):
        assert solve(2) == 9009
