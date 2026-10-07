import pytest

from app.calculator_memento import CalculatorHistory


@pytest.fixture
def history():
    return CalculatorHistory()


def test_save_and_undo(history):
    history.save(8)

    assert history.undo(15) == 8


def test_redo(history):
    history.save(8)

    history.undo(15)

    assert history.redo(8) == 15


def test_undo_with_empty_stack(history):
    assert history.undo(10) == 10


def test_redo_with_empty_stack(history):
    assert history.redo(10) == 10


def test_new_save_clears_redo_stack(history):
    history.save(8)
    history.undo(15)

    history.save(20)

    assert history.redo(20) == 20