import pytest
from app.calculation import Calculation


@pytest.mark.parametrize(
    "operand1, operation, operand2, result",
    [
        (5, "+", 3, 8),
        (10, "-", 4, 6),
        (6, "*", 2, 12),
        (10, "/", 2, 5),
    ],
)
def test_calculation(operand1, operation, operand2, result):
    calculation = Calculation(
        operand1,
        operation,
        operand2,
        result,
    )

    assert calculation.operand1 == operand1
    assert calculation.operation == operation
    assert calculation.operand2 == operand2
    assert calculation.result == result


def test_calculation_string():
    calculation = Calculation(5, "+", 3, 8)

    assert str(calculation) == "5 + 3 = 8"