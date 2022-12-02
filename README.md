# dat-terminal
An interactive customizable terminal for applications that need custom commands.

## Installing
To install the library, you can run the following command:
```
# Linux/macOS
python3 -m pip install dat-terminal

# Windows
py -3 -m pip install dat-terminal
```

## Quick Example
```py
import dat_terminal
import sys


class QuitCommand(dat_terminal.Command):
    def execute(self, user_input: dat_terminal.Input) -> None:
        code = user_input.arguments[0] if user_input.arguments else 0
        sys.exit(code)


dat_terminal.init()

terminal = dat_terminal.DatTerminal()
terminal.invoker.add_command('quit', QuitCommand(), aliases=('q', 'exit'))
terminal.run()

```
