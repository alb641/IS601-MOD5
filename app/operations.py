from abc import ABC, abstractmethod
import math


class OperationStrategy(ABC):
    """Base strategy for calculator operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Execute the operation using two numbers."""
        pass # pragma: no cover


class AdditionStrategy(OperationStrategy):
    """Strategy for addition."""

    def execute(self, a: float, b: float) -> float:
        return a + b


class SubtractionStrategy(OperationStrategy):
    """Strategy for subtraction."""

    def execute(self, a: float, b: float) -> float:
        return a - b


class MultiplicationStrategy(OperationStrategy):
    """Strategy for multiplication."""

    def execute(self, a: float, b: float) -> float:
        return a * b


class DivisionStrategy(OperationStrategy):
    """Strategy for division."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class PowerStrategy(OperationStrategy):
    """Strategy for exponentiation."""

    def execute(self, a: float, b: float) -> float:
        return a ** b


class RootStrategy(OperationStrategy):
    """Strategy for calculating roots."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Root degree cannot be zero.")

        if a < 0 and b % 2 == 0:
            raise ValueError("Cannot calculate an even root of a negative number.")

        return math.copysign(abs(a) ** (1 / b), a) if a < 0 else a ** (1 / b)

class OperationFactory:
    """Creates the appropriate operation strategy."""

    _operations = {
        "+": AdditionStrategy,
        "-": SubtractionStrategy,
        "*": MultiplicationStrategy,
        "/": DivisionStrategy,
        "^": PowerStrategy,
        "root": RootStrategy,
    }

    @classmethod
    def create(cls, operation: str) -> OperationStrategy:
        """Return the strategy associated with an operation."""
        try:
            strategy_class = cls._operations[operation.lower()]
            return strategy_class()
        except KeyError:
            raise ValueError(f"Unsupported operation: {operation}")