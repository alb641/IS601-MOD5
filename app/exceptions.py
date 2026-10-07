class CalculatorError(Exception):
    """Base exception for calculator errors."""


class InvalidOperationError(CalculatorError):
    """Raised when an unsupported operation is requested."""


class InvalidInputError(CalculatorError):
    """Raised when calculator input is invalid."""


class CalculationError(CalculatorError):
    """Raised when a calculation cannot be completed."""