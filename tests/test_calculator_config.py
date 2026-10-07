import pytest

from app.calculator_config import CalculatorConfig


def test_config_defaults():
    config = CalculatorConfig()

    assert config.history_file == "calculator_history.csv"
    assert config.precision == 2
    assert config.validate() is True


def test_config_empty_history_file(monkeypatch):
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "")

    config = CalculatorConfig()

    with pytest.raises(ValueError):
        config.validate()


def test_config_negative_precision(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "-1")

    config = CalculatorConfig()

    with pytest.raises(ValueError):
        config.validate()