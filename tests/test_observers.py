from app.calculation import Calculation
from app.observers import CalculationObserver, CalculatorSubject, Observer


def test_observer_receives_calculation():
    subject = CalculatorSubject()
    observer = CalculationObserver()

    subject.attach(observer)

    calculation = Calculation(5, "+", 3, 8)
    subject.notify(calculation)

    assert observer.calculations == [calculation]


def test_observer_can_be_detached():
    subject = CalculatorSubject()
    observer = CalculationObserver()

    subject.attach(observer)
    subject.detach(observer)

    calculation = Calculation(5, "+", 3, 8)
    subject.notify(calculation)

    assert observer.calculations == []


def test_subject_can_notify_multiple_observers():
    subject = CalculatorSubject()
    observer1 = CalculationObserver()
    observer2 = CalculationObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    calculation = Calculation(5, "+", 3, 8)
    subject.notify(calculation)

    assert observer1.calculations == [calculation]
    assert observer2.calculations == [calculation]


def test_base_observer_requires_update():
    observer = Observer()

    try:
        observer.update(None)
    except NotImplementedError:
        assert True
    else:
        assert False
    