import pandas as pd


class CalculationHistory:
    """Manages calculator calculation history using pandas."""

    def __init__(self):
        """Initialize an empty calculation history."""
        self.history = pd.DataFrame(
            columns=["operand1", "operation", "operand2", "result"]
        )

    def add(self, calculation):
        """Add a calculation to the history."""
        new_row = pd.DataFrame(
            [{
                "operand1": calculation.operand1,
                "operation": calculation.operation,
                "operand2": calculation.operand2,
                "result": calculation.result,
            }]
        )

        self.history = pd.concat(
            [self.history, new_row],
            ignore_index=True
        )

    def clear(self):
        """Clear all calculation history."""
        self.history = pd.DataFrame(
            columns=["operand1", "operation", "operand2", "result"]
        )

    def get_history(self):
        """Return the calculation history."""
        return self.history

    def save(self, filename):
        """Save calculation history to a CSV file."""
        self.history.to_csv(filename, index=False)

    def load(self, filename):
        """Load calculation history from a CSV file."""
        self.history = pd.read_csv(filename)