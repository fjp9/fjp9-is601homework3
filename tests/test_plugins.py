''' This module contains the test cases for the plugins '''
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.exit import ExitCommand
from app.plugins.menu import MenuCommand
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
    menu_command = MenuCommand()
    menu_command.command_handler = command_handler

    # Execute the AddCommand
    menu_command.execute()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert "Available plugins:\n- add\n- subtract\n- multiply\n- divide\n- exit\n" in captured.out, "MenuCommand Output mismatch"
