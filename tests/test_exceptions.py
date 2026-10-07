import pytest

from app.exceptions import (
    CalculatorError,
    InvalidOperationError,
    InvalidInputError,
    CalculationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        CalculatorError,
        InvalidOperationError,
        InvalidInputError,
        CalculationError,
    ],
)
def test_custom_exceptions(exception_class):
    with pytest.raises(exception_class):
        raise exception_class("Test error")