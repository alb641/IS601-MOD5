class CalculatorMemento:
    """Stores a snapshot of the calculator state."""

    def __init__(self, result):
        self.result = result


class CalculatorHistory:
    """Manages calculator states for undo and redo."""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, result):
        """Save the current calculator result."""
        self.undo_stack.append(CalculatorMemento(result))
        self.redo_stack.clear()

    def undo(self, current_result):
        """Undo the most recent state."""
        if not self.undo_stack:
            return current_result

        self.redo_stack.append(CalculatorMemento(current_result))
        memento = self.undo_stack.pop()

        return memento.result

    def redo(self, current_result):
        """Redo the most recent undone state."""
        if not self.redo_stack:
            return current_result

        self.undo_stack.append(CalculatorMemento(current_result))
        memento = self.redo_stack.pop()

        return memento.result