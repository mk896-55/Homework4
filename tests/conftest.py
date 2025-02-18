import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add a custom command-line option to pytest."""
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        type=int,
        help="Number of test cases to generate dynamically"
    )

@pytest.fixture
def num_records(request):
    """Retrieve the number of records specified in the pytest command."""
    return request.config.getoption("--num_records")

@pytest.fixture(params=[
    (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), fake.random_element(["add", "subtract", "multiply", "divide"]))
    for _ in range(10)  # Default 10 cases, will be updated dynamically
])
def generated_test_data(request):
    """Generate test data using Faker."""
    a, b, operation = request.param
    expected = None

    if operation == "add":
        expected = f"The result of {a} add {b} is equal to {a + b}"
    elif operation == "subtract":
        expected = f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == "multiply":
        expected = f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == "divide":
        expected = f"The result of {a} divide {b} is equal to {a // b}" if b != 0 else "An error occurred: Cannot divide by zero"

    return str(a), str(b), operation, expected
