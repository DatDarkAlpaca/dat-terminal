from .commands.invoker import CommandInvoker
from .input_handler import InputHandler
from .colors import ColorHandler
from .config import ConfigHandler


class DatTerminal:
    def __init__(self):
        ColorHandler.initialize()
        ConfigHandler.initialize()

        self.invoker = CommandInvoker()

    def run(self):
        while True:
            user_input = InputHandler.get_input()
            self.invoker.invoke_command(user_input)
