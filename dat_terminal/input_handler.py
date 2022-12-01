from dataclasses import dataclass, field

from .config import ConfigHandler
from .colors import c


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
        prefix = f"{ConfigHandler.get('General', 'PREFIX').response} "
        user_input = input(c(prefix)).split(' ')

        if user_input[0].isspace():
            return NullInput()

        return Input(user_input[0], user_input[1:])
