from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorHistory
from app.exceptions import CalculatorError
from app.history import CalculationHistory
from app.input_validators import validate_number, validate_operation
from app.operations import OperationFactory
from app.observers import CalculationObserver, CalculatorSubject


class Calculator:
    """Facade that provides a simple interface to calculator operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.current_result = None
        self.history = CalculationHistory()
        self.memento = CalculatorHistory()
        self.config = CalculatorConfig()
        self.config.validate()
        self.subject = CalculatorSubject()
        self.observer = CalculationObserver()
        self.subject.attach(self.observer)

    def calculate(self, operand1, operation, operand2):
        """Validate and perform a calculation."""
        try:
            operand1 = validate_number(operand1)
            operand2 = validate_number(operand2)
            operation = validate_operation(operation)

            if self.current_result is not None:
                self.memento.save(self.current_result)

            strategy = OperationFactory.create(operation)
            result = strategy.execute(operand1, operand2)

            calculation = Calculation(
                operand1=operand1,
                operation=operation,
                operand2=operand2,
                result=result,
            )

            self.current_result = result
            self.history.add(calculation)
            self.subject.notify(calculation)

            return calculation

        except CalculatorError:
            raise
        except (ValueError, ZeroDivisionError) as error:
            raise CalculatorError(str(error)) from error

    def undo(self):
        """Undo the most recent calculator state."""
        self.current_result = self.memento.undo(self.current_result)
        return self.current_result

    def redo(self):
        """Redo the most recently undone state."""
        self.current_result = self.memento.redo(self.current_result)
        return self.current_result

    def clear(self):
        """Clear the calculator history and current result."""
        self.current_result = None
        self.history.clear()
        self.memento = CalculatorHistory()

    def get_history(self):
        """Return the calculation history."""
        return self.history.get_history()

    def save_history(self):
        """Save calculation history using the configured filename."""
        self.history.save(self.config.history_file)

    def load_history(self):
        """Load calculation history using the configured filename."""
        self.history.load(self.config.history_file)


def run_repl():
    """Run the calculator command-line interface."""
    calculator = Calculator()

    print("Welcome to the Calculator!")
    print("Type 'help' to see available commands.")

    while True:
        try:
            user_input = input("Calculator> ").strip()

            if not user_input:
                continue

            command = user_input.lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                print("Commands:")
                print("  number operator number - Perform a calculation")
                print("  history - Show calculation history")
                print("  undo - Undo the last calculation")
                print("  redo - Redo the last undone calculation")
                print("  clear - Clear calculation history")
                print("  save - Save history to CSV")
                print("  load - Load history from CSV")
                print("  help - Show this help message")
                print("  exit - Exit the calculator")
                continue

            if command == "history":
                print(calculator.get_history())
                continue

            if command == "undo":
                print(f"Result: {calculator.undo()}")
                continue

            if command == "redo":
                print(f"Result: {calculator.redo()}")
                continue

            if command == "clear":
                calculator.clear()
                print("History cleared.")
                continue

            if command == "save":
                calculator.save_history()
                print("History saved.")
                continue

            if command == "load":
                calculator.load_history()
                print("History loaded.")
                continue

            parts = user_input.split()

            if len(parts) != 3:
                print("Invalid input. Use: number operator number")
                continue

            operand1, operation, operand2 = parts

            calculation = calculator.calculate(
                operand1,
                operation,
                operand2,
            )

            print(f"Result: {calculation.result}")

        except CalculatorError as error:
            print(f"Error: {error}")

        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":  # pragma: no cover
    run_repl()  # pragma: no cover