import logging


class ColorFormatter(logging.Formatter):
    def format(self, record):
    '''
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
    '''
    pass

