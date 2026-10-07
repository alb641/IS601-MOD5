class Observer:
    """Base observer class."""

    def update(self, calculation):
        """Receive a calculation update."""
        raise NotImplementedError


class CalculationObserver(Observer):
    """Observer that tracks calculator updates."""

    def __init__(self):
        self.calculations = []

    def update(self, calculation):
        """Store a calculation when notified."""
        self.calculations.append(calculation)


class CalculatorSubject:
    """Subject that notifies observers of new calculations."""

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        """Attach an observer."""
        self.observers.append(observer)

    def detach(self, observer):
        """Detach an observer."""
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, calculation):
        """Notify all attached observers."""
        for observer in self.observers:
            observer.update(calculation)