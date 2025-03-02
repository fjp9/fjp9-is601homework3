import logging
from app.commands import Command
from app.commands import CommandHandler


class SubtractCommand(Command):
    def execute(self):
        try:
            a, b = input("Enter two numbers separated by space: ").split()
            logging.info(f"Subtract command called with {a} and {b}")
            CommandHandler.calculate_and_print(a, b, 'subtract')
        except ValueError:
            print("Please enter two numbers separated by space.")
            logging.error("Invalid input.")
        return
