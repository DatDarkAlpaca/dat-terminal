import logging
import logging.config
import yaml

from .colors import ColorType, colored, ColorEnum, c


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]


class ColorFormatter(logging.Formatter):
    def format(self, record):
        format_color = {
            logging.DEBUG: ColorType.PRIMARY,
            logging.INFO: ColorType.PRIMARY,
            logging.WARNING: ColorType.WARNING,
            logging.ERROR: ColorType.ERROR,
            logging.CRITICAL: ColorType.ERROR,
        }

        date_text = colored('%(asctime)s', ColorEnum.GREEN)
        message = c('%(message)s', ColorType.PRIMARY)
        logger_name = c('%(name)s', ColorType.SECONDARY)
        level = c('%(levelname)s', format_color[record.levelno])

        log_format = f"{date_text} | {colored('[', ColorEnum.WHITE)}" \
                     f"{level}{colored(']', ColorEnum.WHITE)} {logger_name}: {message}"

        formatter = logging.Formatter(log_format)
        return formatter.format(record)


class Logger(metaclass=Singleton):
    _logger: logging.Logger = None

    def __init__(self):
        with open('logger.yaml', mode='r', encoding='utf-8') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

        Logger._logger = logging.getLogger()

    @classmethod
    def info(cls, message: str):
        cls._logger.warning(message)



