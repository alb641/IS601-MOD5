# IS601 Module 5 - Enhanced Calculator Application with Advanced Design Patterns and pandas

An enhanced Python command-line calculator demonstrating object-oriented programming, design patterns, pandas-based history management, automated testing, configuration management, error handling, and continuous integration.

## Features

* Addition, subtraction, multiplication, division, power, and root operations
* Interactive command-line REPL
* Calculation history stored using pandas DataFrame
* CSV save and load functionality
* Automatic history saving after calculations
* Undo and redo functionality
* Configuration using environment variables and `.env`
* Input validation and error handling
* Comprehensive automated testing with pytest
* 100% test coverage
* GitHub Actions continuous integration

## Design Patterns

This project demonstrates the following design patterns:

### Strategy Pattern

Different calculator operations are implemented as separate strategy classes. This allows operations to be selected and executed without placing all calculation logic in one class.

### Factory Pattern

`OperationFactory` creates the appropriate operation strategy based on the requested operation.

### Facade Pattern

The `Calculator` class provides a simple interface for performing calculations while coordinating validation, operations, history, configuration, and notifications.

### Memento Pattern

The calculator uses mementos to store calculator states and support undo and redo functionality.

### Observer Pattern

The calculator uses a subject and observer to notify observers whenever a new calculation is performed.

## Project Structure

```text
IS601-MOD5/
│
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── observers.py
│   └── operations.py
│
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_calculator_repl.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   ├── test_observers.py
│   └── test_operations.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/alb641/IS601-MOD5.git
cd IS601-MOD5
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Calculator

Start the calculator with:

```bash
python -m app.calculator_repl
```

The calculator will display:

```text
Welcome to the Calculator!
Type 'help' to see available commands.
```

## Cal
