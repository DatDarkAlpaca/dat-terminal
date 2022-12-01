# dat-terminal
An interactive customizable terminal for applications that need custom commands.

Quick example:

```py
# Dat Terminal:
from dat_terminal import DatTerminal

from dat_terminal.commands import Command
from dat_terminal.input_handler import Input
from dat_terminal.colors import ColorType, c


class QuitCommand(Command):
    def execute(self, user_input: Input) -> None:
        print(c('Bye bye!', ColorType.WARNING))

        import sys
        code = user_input.arguments[0] if user_input.arguments else 0
        sys.exit(code)


class EchoCommand(Command):
    def execute(self, user_input: Input) -> None:
        text = ''.join(user_input.arguments)
        print(c(text))


def main():
    terminal = DatTerminal()
    terminal.invoker.add_command(name='quit', aliases=('exit', 'leave'), command=QuitCommand())
    terminal.invoker.add_command(name='echo', aliases='say', command=EchoCommand())

    terminal.run()


if __name__ == '__main__':
    main()
```
