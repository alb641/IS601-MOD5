import os

from dotenv import load_dotenv


class CalculatorConfig:
    """Manages calculator configuration settings."""

    def __init__(self):
        """Load configuration from environment variables."""
        load_dotenv()

        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            "calculator_history.csv",
        )
        self.precision = int(
            os.getenv("CALCULATOR_PRECISION", "2")
        )

    def validate(self):
        """Validate calculator configuration."""
        if not self.history_file:
            raise ValueError("History file cannot be empty.")

        if self.precision < 0:
            raise ValueError("Precision cannot be negative.")

        return True