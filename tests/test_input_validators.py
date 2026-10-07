import pytest

from app.exceptions import InvalidInputError
from app.input_validators import validate_number, validate_operation


@pytest.mark.parametrize(
    "value, expected",
    [
        ("5", 5.0),
        ("10", 10.0),
        ("3.14", 3.14),
        ("-7", -7.0),
    ],
)
def test_validate_number(value, expected):
    assert validate_number(value) == expected


def test_invalid_number():
    with pytest.raises(InvalidInputError):
        validate_number("hello")


@pytest.mark.parametrize(
    "operation",
    ["+", "-", "*", "/", "^", "root"],
)
def test_validate_operation(operation):
    assert validate_operation(operation) == operation


def test_validate_operation_uppercase_root():
    assert validate_operation("ROOT") == "root"


def test_invalid_operation():
    with pytest.raises(InvalidInputError):
        validate_operation("%")