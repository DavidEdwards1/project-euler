"""
In the tests we combine traditional unit testing approaches with property-based
testing via hypothesis.

In organsing the tests we have opted for a class per function under test and
also a separate class for unit and property based tests.

The `is_multiple_of` function is a nice one to property test as it has the
non-trivial property where it should return True if n and n*x (where x is any int)
is passed to it.

The use of hypothesis immediately highlighted a problem with `is_multiple_of`,
namely what if n is 0? This raises a `ZeroDivisionError` and shows that actually
the type constraint is not tight enough: we have said that `is_multiple_of` accepts
integers but that is not the case. It was really written for _Natural Numbers_.
Is this problem solvable in Python? Can we make a NaturalNumber type? Or is it
a class with a custom validator? This really seems important in a data validation
type question. In the first instance we can add a min to the strategy to at least
document the expected input range in the tests.

I suppose here the issue is that `is_multiple_of` is a _partial_ function on the
supplied input domain (of integers).

A follow-up question with interesting ramifications: can we use the type annotations
of the method under test to specify strategies? So if we annotate with `int`
then we run tests that use `strategies.integers` as the input for that parameter.

The property based testing approach also threw up an issue with the solve
implementation: it is slow as N grows - hence the need for the different algoroithmic
approach presented by Project Euler.

"""
from hypothesis import given, strategies

from project_euler.problem_1 import is_multiple_of, is_multiple_ofs, solve


class TestUnitIsMultipleOf:
    def test_returns_true_when_is_multiple_of(self):
        assert is_multiple_of(3, 3) == True
        assert is_multiple_of(5, 5) == True

    def test_returns_false_when_not_is_multiple_of(self):
        assert is_multiple_of(5, 729) == False
        assert is_multiple_of(3, 65) == False


class TestUnitIsMultipleOfs:
    def test_returns_true_when_element_is_multiple_of(self):
        assert is_multiple_ofs([3, 5], 20) == True
        assert is_multiple_ofs([3, 5], 729) == True

    def test_returns_false_when_element_not_is_multiple_of(self):
        assert is_multiple_ofs([3, 5], 17) == False
        assert is_multiple_ofs([3, 5], 121) == False


class TestUnitSolve:
    def test_solve_gives_expected_value(self):
        assert solve(10) == 23


class TestPropertyIsMultipleOf:
    @given(strategies.integers(min_value=1), strategies.integers())
    def test_n_divides_n_multipled_by_value(self, n: int, x: int):
        assert is_multiple_of(n, n * x) == True


class TestPropertySolve:
    @given(strategies.integers(min_value=2, max_value=100_000))
    def test_solve_runs_without_error(self, max_n: int):
        assert type(solve(max_n)) == int
