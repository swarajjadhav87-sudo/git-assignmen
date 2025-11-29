# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, square, sqrt

# Test for addition
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add("2", "3") == 5  # Test string inputs
    assert add("two", "three") == "Error! Invalid input."

# Test for subtraction
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract("5", "3") == 2  # Test string inputs
    assert subtract("five", "three") == "Error! Invalid input."

# Test for multiplication
def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-4, 5) == -20
    assert multiply(0, 100) == 0
    assert multiply("4", "5") == 20  # Test string inputs
    assert multiply("four", "five") == "Error! Invalid input."

# Test for division
def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error! Division by zero."
    assert divide(5, "2") == 2.5  # Test string inputs
    assert divide("five", "two") == "Error! Invalid input."

# Test for square
def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square("4") == 16  # Test string inputs
    assert square("four") == "Error! Invalid input."

# Test for square root
def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert sqrt(-4) == "Error! Cannot take square root of a negative number."
    assert sqrt("9") == 3  # Test string inputs
    assert sqrt("nine") == "Error! Invalid input."

