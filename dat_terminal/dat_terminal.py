from .commands.invoker import CommandInvoker
from .input_handler import InputHandler


class DatTerminal:
    def __init__(self):
        self.invoker = CommandInvoker()

    def run(self):
        while True:
            user_input = InputHandler.get_input()
            self.invoker.invoke_command(user_input)
