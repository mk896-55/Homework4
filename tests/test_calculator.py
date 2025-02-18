from faker import Faker
import pytest
from calculator import calculate  # Import your calculator function

fake = Faker()

@pytest.mark.parametrize("a, b, operation, expected", [
    (str(fake.random_int(min=1, max=100)), str(fake.random_int(min=1, max=100)), 'add', None),  # Expected will be computed
    (str(fake.random_int(min=1, max=100)), str(fake.random_int(min=1, max=100)), 'subtract', None),
    (str(fake.random_int(min=1, max=10)), str(fake.random_int(min=1, max=10)), 'multiply', None),
    (str(fake.random_int(min=10, max=100)), str(fake.random_int(min=1, max=10)), 'divide', None),
])
def test_calculator(a, b, operation, expected):
    expected = f"The result of {a} {operation} {b} is equal to {eval(f'{a}{operation}{b}')}"

    if operation == 'divide' and int(b) == 0:
        expected = "An error occurred: Cannot divide by zero"

    result = calculate(a, b, operation)
    assert result == expected