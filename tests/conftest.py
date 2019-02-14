import pytest


@pytest.fixture(scope="session")
def fibonacci():
    def _fib(number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fib(number - 1) + fib(number - 2)

    def fib(number):
        sequence = []
        if number > 0:
            sequence.extend(fib(number - 1))

        sequence.append(_fib(number))
        return sequence

    return fib
