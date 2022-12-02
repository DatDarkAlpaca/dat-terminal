import re
import colorama
from termcolor import colored
from dataclasses import dataclass, field

from .themes import load_theme, Theme


__all__ = ['c', 'set_theme']

# Initialization:
colorama.just_fix_windows_console()

# Theme:
theme = Theme()


def set_theme(theme_name: str):
    global theme
    theme = load_theme(theme_name)


# Todo: refactor
def c(text: str) -> str:
    result = text

    # Colors:
    for key, color in theme.colors.items():
        styled_portion = re.findall(f"<{key}>(.*?)</{key}>", text)

        if not styled_portion:
            continue

        for portion in styled_portion:
            result = re.sub(f"<{key}>(.*?)</{key}>",
                            colored(portion, color=color),
                            result, 1)

    # Highlights
    for key, highlight in theme.highlights.items():
        styled_portion = re.findall(f"<{key}>(.*?)</{key}>", text)

        if not styled_portion:
            continue

        for portion in styled_portion:
            result = re.sub(f"<{key}>(.*?)</{key}>",
                            colored(portion, on_color=highlight),
                            result, 1)

    # Attributes:
    for key, attributes in theme.attributes.items():
        styled_portion = re.findall(f"<{key}>(.*?)</{key}>", text)

        if not styled_portion:
            continue

        for portion in styled_portion:
            result = re.sub(f"<{key}>(.*?)</{key}>",
                            colored(portion, attrs=attributes),
                            result, 1)

    # Custom Themes:
    for key, style in theme.content.items():
        styled_portion = re.findall(f"<{key}>(.*?)</{key}>", text)

        if not styled_portion:
            continue

        for portion in styled_portion:
            result = re.sub(f"<{key}>(.*?)</{key}>",
                            colored(portion, color=style.color, on_color=style.highlight, attrs=style.attributes),
                            result, 1)

    return result


def primary(text: str) -> str:
    return c(f"<primary>{text}</primary>")

