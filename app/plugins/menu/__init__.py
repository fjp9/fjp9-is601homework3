from app.commands import Command
from app.commands import CommandHandler

class MenuCommand(Command):
    def execute(self, *args):
        print("Available plugins:")
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")
