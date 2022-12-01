from enum import Enum
from colorclass import Color

from .config import ConfigHandler


class ColorEnum(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7

    def __str__(self):
        return f"auto{self.name.lower()}"


class ColorType(Enum):
    PRIMARY = 0
    SECONDARY = 1
    WARNING = 2
    ERROR = 3


class ColorHandler:
    color_palette = {
        ColorType.PRIMARY: ColorEnum.WHITE,
        ColorType.SECONDARY: ColorEnum.BLUE,
        ColorType.WARNING: ColorEnum.YELLOW,
        ColorType.ERROR: ColorEnum.RED,
    }

    @staticmethod
    def initialize():
        # Todo: default colors if the settings are wrong
        primary = ColorEnum[ConfigHandler.general('PRIMARY_COLOR').response.upper()]
        secondary = ColorEnum[ConfigHandler.general('SECONDARY_COLOR').response.upper()]
        warning = ColorEnum[ConfigHandler.general('WARNING_COLOR').response.upper()]
        error = ColorEnum[ConfigHandler.general('ERROR_COLOR').response.upper()]

        ColorHandler.color_palette = {
            ColorType.PRIMARY: primary,
            ColorType.SECONDARY: secondary,
            ColorType.WARNING: warning,
            ColorType.ERROR: error
        }

    @staticmethod
    def set_primary_color(color: str) -> None:
        try:
            ColorHandler.color_palette[ColorType.PRIMARY] = ColorEnum[color.upper()]
            ConfigHandler.set('General', 'PRIMARY_COLOR', color.lower())
        except KeyError:
            # Todo: handle invalid color
            return

    @staticmethod
    def set_secondary_color(color: str) -> None:
        try:
            ColorHandler.color_palette[ColorType.SECONDARY] = ColorEnum[color.upper()]
            ConfigHandler.set('General', 'PRIMARY_COLOR', color.lower())
        except KeyError:
            # Todo: handle invalid color
            return

    @staticmethod
    def set_warning_color(color: str) -> None:
        try:
            ColorHandler.color_palette[ColorType.WARNING] = ColorEnum[color.upper()]
            ConfigHandler.set('General', 'WARNING_COLOR', color.lower())
        except KeyError:
            # Todo: handle invalid color
            return

    @staticmethod
    def set_error_color(color: str) -> None:
        try:
            ColorHandler.color_palette[ColorType.ERROR] = ColorEnum[color.upper()]
            ConfigHandler.set('General', 'WARNING_COLOR', color.lower())
        except KeyError:
            # Todo: handle invalid color
            return


# Shorthand function that takes a text and applies a certain color to it:
def c(text: str, color_type: ColorType = ColorType.PRIMARY) -> str:
    color = str(ColorHandler.color_palette[color_type])
    color_start = '{' + color + '}'
    color_end = '{/' + color + '}'
    return Color(f"{color_start}{text}{color_end}")


def colored(text: str, color_name: ColorEnum):
    color = str(color_name)

    color_start = '{' + color + '}'
    color_end = '{/' + color + '}'
    return Color(f"{color_start}{text}{color_end}")
