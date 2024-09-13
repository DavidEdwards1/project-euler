from project_euler.problem_2 import fibonacci, fibonacci_recursive

def test_fibonacci_recursive_small_integer(benchmark):
    benchmark(fibonacci_recursive, 5)

def test_fibonacci_small_integer(benchmark):
    benchmark(fibonacci, 5)

def test_fibonacci_medium_integer(benchmark):
    benchmark(fibonacci, 15)
