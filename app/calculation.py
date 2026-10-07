from dataclasses import dataclass


@dataclass
class Calculation:
    """Represents a single calculator operation."""

    operand1: float
    operation: str
    operand2: float
    result: float

    def __str__(self) -> str:
        """Return a readable representation of the calculation."""
        return (
            f"{self.operand1} {self.operation} "
            f"{self.operand2} = {self.result}"
        )