from ..input_handler import Input
from .command import Command

from dat_terminal.config import read_entry


class CommandInvoker:
    def __init__(self):
        self.command_list = {}

    def add_command(self, name: str, command: Command, aliases: tuple[str] = None) -> None:
        if aliases:
            for command_name in aliases:
                self.command_list[command_name] = command
        
        self.command_list[name] = command

    def invoke_command(self, user_input: Input) -> None:
        if not user_input.command_identifier:
            return

        command = self.command_list.get(user_input.command_identifier)

        if not command and read_entry('General', 'enable-warnings').as_bool():
            # Todo: use the logger to display warnings
            print('Warning: command does not exist.')
            return

        command.execute(user_input)
