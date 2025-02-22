import sys
from app.commands import Command
from app.commands import CommandHandler


class AddCommand(Command):
    def execute(self):
        try:
            a, b = input("Enter two numbers separated by space: ").split()
            CommandHandler.calculate_and_print(a, b, 'add')
        except ValueError:
            print("Please enter two numbers separated by space.")
        return
