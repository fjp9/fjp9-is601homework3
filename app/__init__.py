import sys
from calculator import Calculator
from app.commands import CommandHandler
from app.commands.add import AddCommand 
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from decimal import Decimal, InvalidOperation

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("exit", ExitCommand())
        print("Welcome to the calculator app. Type 'exit' to quit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())
