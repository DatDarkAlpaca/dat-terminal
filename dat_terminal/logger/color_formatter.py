import logging
from dat_terminal.colors import c, use_prop


class ColorFormatter(logging.Formatter):
    def format(self, record):
        format_prop = {
            logging.DEBUG: 'primary',
            logging.INFO: 'primary',
            logging.WARNING: 'warning',
            logging.ERROR: 'error',
            logging.CRITICAL: 'critical',
        }
        date_text = c('<green>%(asctime)s</green>')
        message = c('<primary>%(message)s</primary>')
        logger_name = c('<magenta>%(name)s</magenta>')

        level_prop = format_prop[record.levelno]
        level = use_prop('%(levelname)s', level_prop)

        log_format = f"{date_text} | [{level}] {logger_name}: {message}"
        formatter = logging.Formatter(log_format)

        return formatter.format(record)
