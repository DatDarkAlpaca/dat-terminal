from .dat_terminal import DatTerminal
from .input_handler import Input, InputHandler

from .commands import *
from .logger import *
from .utils import *
from .colors import *
from .config import *
from .paths import *
from .themes import *


def init():
    config.create_default_config_file()
    themes.set_theme('DefaultTheme')
