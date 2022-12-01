from typing import Protocol
from ..input_handler import Input


class Command(Protocol):
    def execute(self, user_input: Input) -> None:
        ...
