from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def calculate_and_print(a, b, operation_name):
        operation_mappings = {
            'add': Calculator.add,
            'subtract': Calculator.subtract,
            'multiply': Calculator.multiply,
            'divide': Calculator.divide
        }

        # Unified error handling for decimal conversion
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            result = operation_mappings.get(operation_name) # Use get to handle unknown operations
            if result:
                print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
            else:
                print(f"Unknown operation: {operation_name}")
        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}")

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")