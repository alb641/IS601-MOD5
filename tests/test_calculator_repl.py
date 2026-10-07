import pytest
from unittest.mock import patch

from app.calculator_repl import Calculator, run_repl
from app.exceptions import CalculatorError


def test_calculate_addition():
    calculator = Calculator()

    calculation = calculator.calculate(5, "+", 3)

    assert calculation.result == 8
    assert calculator.current_result == 8


@pytest.mark.parametrize(
    "operand1, operation, operand2, expected",
    [
        (10, "-", 4, 6),
        (6, "*", 2, 12),
        (10, "/", 2, 5),
        (2, "^", 3, 8),
        (9, "root", 2, 3),
    ],
)
def test_calculate_operations(operand1, operation, operand2, expected):
    calculator = Calculator()

    calculation = calculator.calculate(
        operand1,
        operation,
        operand2,
    )

    assert calculation.result == expected


def test_history():
    calculator = Calculator()

    calculator.calculate(5, "+", 3)

    history = calculator.get_history()

    assert len(history) == 1
    assert history.iloc[0]["result"] == 8


def test_undo_and_redo():
    calculator = Calculator()

    calculator.calculate(5, "+", 3)
    calculator.calculate(10, "*", 2)

    assert calculator.undo() == 8
    assert calculator.redo() == 20


def test_clear():
    calculator = Calculator()

    calculator.calculate(5, "+", 3)
    calculator.clear()

    assert calculator.current_result is None
    assert calculator.get_history().empty


def test_invalid_input():
    calculator = Calculator()

    with pytest.raises(Exception):
        calculator.calculate("hello", "+", 3)


def test_repl_help_and_exit(capsys):
    with patch("builtins.input", side_effect=["help", "exit"]):
        run_repl()

    output = capsys.readouterr().out

    assert "Commands:" in output
    assert "Goodbye!" in output


def test_repl_calculation_and_history(capsys):
    with patch(
        "builtins.input",
        side_effect=["5 + 3", "history", "exit"],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "Result: 8.0" in output
    assert "8.0" in output


def test_repl_undo_redo(capsys):
    with patch(
        "builtins.input",
        side_effect=[
            "5 + 3",
            "10 * 2",
            "undo",
            "redo",
            "exit",
        ],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "Result: 8.0" in output
    assert "Result: 20.0" in output


def test_repl_clear(capsys):
    with patch(
        "builtins.input",
        side_effect=["5 + 3", "clear", "exit"],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "History cleared." in output


def test_repl_invalid_input(capsys):
    with patch(
        "builtins.input",
        side_effect=["hello", "exit"],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "Invalid input." in output


def test_repl_invalid_calculation(capsys):
    with patch(
        "builtins.input",
        side_effect=["5 / 0", "exit"],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "Error:" in output


def test_repl_save_and_load(capsys):
    with patch(
        "builtins.input",
        side_effect=[
            "5 + 3",
            "save",
            "clear",
            "load",
            "exit",
        ],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "History saved." in output
    assert "History cleared." in output
    assert "History loaded." in output


def test_repl_empty_input(capsys):
    with patch(
        "builtins.input",
        side_effect=["", "exit"],
    ):
        run_repl()

    output = capsys.readouterr().out

    assert "Goodbye!" in output


def test_repl_value_error_handler(capsys):
    with patch(
        "app.calculator_repl.Calculator.calculate",
        side_effect=ValueError("Test value error"),
    ):
        with patch(
            "builtins.input",
            side_effect=["5 + 3", "exit"],
        ):
            run_repl()

    output = capsys.readouterr().out

    assert "Error: Test value error" in output


def test_repl_calculator_error_handler(capsys):
    with patch(
        "app.calculator_repl.Calculator.calculate",
        side_effect=CalculatorError("Test calculator error"),
    ):
        with patch(
            "builtins.input",
            side_effect=["5 + 3", "exit"],
        ):
            run_repl()

    output = capsys.readouterr().out

    assert "Error: Test calculator error" in output


def test_calculate_autosaves_history(tmp_path):
    calculator = Calculator()
    calculator.config.history_file = str(tmp_path / "history.csv")

    calculator.calculate(5, "+", 3)

    assert (tmp_path / "history.csv").exists()