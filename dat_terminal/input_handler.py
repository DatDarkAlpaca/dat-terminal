from dataclasses import dataclass, field

from .config import read_entry
from .colors import primary


@dataclass
class Input:
    command_identifier: str
    arguments: list[str] = field(default_factory=list)


@dataclass
class NullInput(Input):
    command_identifier: str = ''
    arguments: list[str] = field(default_factory=list)


class InputHandler:
    @staticmethod
    def get_input() -> Input:
        prefix = f"{read_entry('General', 'prefix').response} "
        user_input = input(primary(prefix)).split(' ')

        if user_input[0].isspace():
            return NullInput()

        return Input(user_input[0], user_input[1:])
