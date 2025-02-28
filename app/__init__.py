import sys
import importlib
import pkgutil
from calculator import Calculator
from app.commands import CommandHandler
from app.commands import Command
from decimal import Decimal, InvalidOperation

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item is not Command:  # Ensure it's a Command subclass
                            plugin_instance = item()
                            plugin_instance.command_handler = self.command_handler
                            self.command_handler.register_command(plugin_name, plugin_instance)
                    except TypeError:
                        print(item_name)  # If item is not a class or unrelated class, just ignore
    
    def start(self):
        # Register commands here
        self.load_plugins()
        print("Welcome to the calculator app. Type 'exit' to quit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())
