import sys
from app.commands import Command
from app.commands import CommandHandler


class DivideCommand(Command):
    def execute(self):
        a, b = input("Enter two numbers separated by space: ").split()
        CommandHandler.calculate_and_print(a, b, 'divide')
        return