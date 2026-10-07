import pytest

from app.operations import (
    AdditionStrategy,
    SubtractionStrategy,
    MultiplicationStrategy,
    DivisionStrategy,
    PowerStrategy,
    RootStrategy,
    OperationFactory,
)


@pytest.mark.parametrize(
    "strategy, a, b, expected",
    [
        (AdditionStrategy(), 5, 3, 8),
        (SubtractionStrategy(), 5, 3, 2),
        (MultiplicationStrategy(), 5, 3, 15),
        (DivisionStrategy(), 6, 3, 2),
        (PowerStrategy(), 2, 3, 8),
        (RootStrategy(), 9, 2, 3),
    ],
)
def test_operations(strategy, a, b, expected):
    assert strategy.execute(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        DivisionStrategy().execute(10, 0)


def test_root_zero_degree():
    with pytest.raises(ValueError):
        RootStrategy().execute(10, 0)


def test_even_root_of_negative_number():
    with pytest.raises(ValueError):
        RootStrategy().execute(-16, 2)


@pytest.mark.parametrize(
    "operation",
    ["+", "-", "*", "/", "^", "root"],
)
def test_operation_factory(operation):
    strategy = OperationFactory.create(operation)

    assert strategy is not None


def test_invalid_operation_factory():
    with pytest.raises(ValueError):
        OperationFactory.create("%")
