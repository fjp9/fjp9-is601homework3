from app.commands import Command
from app.commands import CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        for command in self.command_handler.commands:
            print(command)
        return