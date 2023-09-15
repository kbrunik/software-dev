import pytest
from research_software_dev.guides.testing.calculator import Calculator

# Fixture to set up the Calculator instance before tests
@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    result = calculator.add(1, 2)
    assert result == 3, f"Expected 3 but got {result}"

def test_subtraction(calculator):
    result = calculator.subtract(5, 3)
    assert result == 2, f"Expected 2 but got {result}"

def test_multiplication(calculator):
    result = calculator.multiply(3, 4)
    assert result == 12, f"Expected 12 but got {result}"
