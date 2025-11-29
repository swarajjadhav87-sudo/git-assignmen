# calculator.py

def add(a, b):
    """Add two numbers."""
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        return "Error! Invalid input."

def subtract(a, b):
    """Subtract two numbers."""
    try:
        return float(a) - float(b)
    except (ValueError, TypeError):
        return "Error! Invalid input."

def multiply(a, b):
    """Multiply two numbers."""
    try:
        return float(a) * float(b)
    except (ValueError, TypeError):
        return "Error! Invalid input."

def divide(a, b):
    """Divide two numbers, returns error message if division by zero."""
    try:
        a, b = float(a), float(b)
        if b == 0:
            return "Error! Division by zero."
        return a / b
    except (ValueError, TypeError):
        return "Error! Invalid input."

def square(a):
    """Return the square of a number."""
    try:
        return float(a) ** 2
    except (ValueError, TypeError):
        return "Error! Invalid input."

def sqrt(a):
    """Return the square root of a number."""
    try:
        if a < 0:
            return "Error! Cannot take square root of a negative number."
        return a ** 0.5
    except (ValueError, TypeError):
        return "Error! Invalid input."

