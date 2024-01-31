import pytest
from test2 import add, subtract, multiply, divide


# Check if it is added properly
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(0, 5) == 0

    # with pytest.raises(ValueError):
    #     # Intentionally introduce an error by passing 0 as the divisor
    #     divide(3, 0)


# Check if it is  properly proudce an error


def test_add_string_expected_exception():
    with pytest.raises(TypeError):
        # Intentionally introduce an error by passing a string
        add(3, "0")


def test_subtract_string_expected_exception():
    with pytest.raises(TypeError):
        subtract(3, "0")


def test_multiply_string_expected_exception():
    with pytest.raises(TypeError):
        multiply(3, "0")


def test_multiply_string_expected_exception():
    assert multiply(3, "0") == "000"


def test_divide_string_expected_exception():
    with pytest.raises(TypeError):
        divide(3, "0")

