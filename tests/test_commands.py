""" This module contains the test cases for the commands module """
import pytest
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand
from app.commands import CommandHandler

def test_add_command(monkeypatch, capsys):
    """ Test the AddCommand execute method """
    # Simulate user input
    inputs = iter(['3 5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    add_command = AddCommand()

    # Execute the AddCommand
    add_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "The result of 3 add 5 is equal to 8\n" in captured.out, "AddCommand Output mismatch"

def test_add_command_invalid_input(monkeypatch, capsys):
    """ Test the AddCommand execute method with invalid input """
    # Simulate user input
    inputs = iter(['2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    add_command = AddCommand()

    # Execute the AddCommand
    add_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "Please enter two numbers separated by space.\n" in captured.out, "AddCommand Output mismatch"

def test_divide_command(monkeypatch, capsys):
    """ Test the DivideCommand execute method """
    # Simulate user input
    inputs = iter(['10 5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    divide_command = DivideCommand()

    # Execute the AddCommand
    divide_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "The result of 10 divide 5 is equal to 2\n" in captured.out, "DivideCommand Output mismatch"

def test_divide_command_invalid_input(monkeypatch, capsys):
    """ Test the DivideCommand execute method with invalid input """
    # Simulate user input
    inputs = iter(['10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    divide_command = DivideCommand()

    # Execute the AddCommand
    divide_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "Please enter two numbers separated by space.\n" in captured.out, "DivideCommand error message mismatch"

def test_multiply_command(monkeypatch, capsys):
    """ Test the MultiplyCommand execute method """
    # Simulate user input
    inputs = iter(['3 5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    multiply_command = MultiplyCommand()

    # Execute the AddCommand
    multiply_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "The result of 3 multiply 5 is equal to 15\n" in captured.out, "MultiplyCommand Output mismatch"

def test_multiply_command_invalid_input(monkeypatch, capsys):
    """ Test the MultiplyCommand execute method with invalid input """
    # Simulate user input
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    multiply_command = MultiplyCommand()

    # Execute the AddCommand
    multiply_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "Please enter two numbers separated by space.\n" in captured.out, "MultiplyCommand error message mismatch"

def test_subtract_command(monkeypatch, capsys):
    """ Test the SubtractCommand execute method """
    # Simulate user input
    inputs = iter(['10 5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    subtract_command = SubtractCommand()

    # Execute the AddCommand
    subtract_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "The result of 10 subtract 5 is equal to 5\n" in captured.out, "SubtractCommand Output mismatch"

def test_subtract_command_invalid_input(monkeypatch, capsys):
    """ Test the SubtractCommand execute method with invalid input """
    # Simulate user input
    inputs = iter(['10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    # command_handler = CommandHandler()
    subtract_command = SubtractCommand()

    # Execute the AddCommand
    subtract_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "Please enter two numbers separated by space.\n" in captured.out, "SubtractCommand error message mismatch"

def test_menu_command(monkeypatch, capsys):
    """ Test the MenuCommand execute method """
    # Simulate user input
    inputs = iter(['menu'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create a CommandHandler and AddCommand instance
    command_handler = CommandHandler()
    command_handler.register_command("add", AddCommand())
    command_handler.register_command("subtract", SubtractCommand())
    command_handler.register_command("multiply", DivideCommand())
    command_handler.register_command("divide", MultiplyCommand())
    command_handler.register_command("exit", ExitCommand())
    menu_command = MenuCommand(command_handler)

    # Execute the AddCommand
    menu_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "add\nsubtract\nmultiply\ndivide\nexit" in captured.out, "MenuCommand Output mismatch"

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    """
    Test the calculate_and_print function with different inputs and operations.
    """
    CommandHandler.calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
