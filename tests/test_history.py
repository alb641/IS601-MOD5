import pandas as pd

from app.calculation import Calculation
from app.history import CalculationHistory


def test_history_starts_empty():
    history = CalculationHistory()

    assert history.get_history().empty


def test_add_calculation():
    history = CalculationHistory()
    calculation = Calculation(5, "+", 3, 8)

    history.add(calculation)

    data = history.get_history()

    assert len(data) == 1
    assert data.iloc[0]["result"] == 8


def test_clear_history():
    history = CalculationHistory()
    history.add(Calculation(5, "+", 3, 8))

    history.clear()

    assert history.get_history().empty


def test_save_and_load_history(tmp_path):
    history = CalculationHistory()
    history.add(Calculation(5, "+", 3, 8))

    filename = tmp_path / "history.csv"
    history.save(filename)

    loaded_history = CalculationHistory()
    loaded_history.load(filename)

    pd.testing.assert_frame_equal(
        history.get_history(),
        loaded_history.get_history(),
        check_dtype=False,
    )