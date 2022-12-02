from dat_terminal.config import create_default_config_file
from dat_terminal import DatTerminal
from dat_terminal.colors import c, set_theme


def main():
    set_theme('DefaultTheme')

    print(c('<red>[</red> <warning>!</warning> <red>]</red>: You\'re gay.'))
    create_default_config_file()

    terminal = DatTerminal()
    terminal.run()


if __name__ == '__main__':
    main()
