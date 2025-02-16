"""
This module contains pytest configuration and fixtures for generating test data for calculator operations.

Functions:
    generate_test_data(num_records):
        Generates test data for calculator operations including add, subtract, multiply, and divide.
    
    pytest_addoption(parser):
        Adds a command line option to specify the number of test records to generate.
    
    pytest_generate_tests(metafunc):
        Generates test cases dynamically based on the specified number of test records.
"""
# pylint: disable=unused-import
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generates test data for Calculator and Calculation tests.

    Args:
        num_records (int): The number of test records to generate.

    Yields:
        tuple: A tuple containing:
            - a (Decimal): The first operand.
            - b (Decimal): The second operand.
            - operation_name (str): The name of the operation ('add', 'subtract', 'multiply', 'divide').
            - operation_func (function): The function corresponding to the operation.
            - expected (Decimal or str): The expected result of the operation, or "ZeroDivisionError" if a division by zero is expected.
    """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide: # pylint: disable=comparison-with-callable
            b = Decimal('1') if b == Decimal('0') else b

        try:
            if operation_func == divide and b == Decimal('0'): # pylint: disable=comparison-with-callable
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Adds a command line option to specify the number of test records to generate.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generates test cases dynamically based on the specified number of test records.
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
