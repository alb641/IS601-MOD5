from app.exceptions import InvalidInputError


def validate_number(value):
    """Validate and convert a value to a number."""
    try:
        return float(value)
    except (ValueError, TypeError):
        raise InvalidInputError(f"Invalid number: {value}")


def validate_operation(operation):
    """Validate a calculator operation."""
    valid_operations = ["+", "-", "*", "/", "^", "root"]

    if operation.lower() not in valid_operations:
        raise InvalidInputError(f"Invalid operation: {operation}")

    return operation.lower()