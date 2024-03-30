import logging
import sys
from logging.handlers import RotatingFileHandler

import colorlog


class LogHandler:
    def __init__(self, log_file=None, log_level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        if log_file:
            file_handler = RotatingFileHandler(
                log_file, maxBytes=1024 * 1024, backupCount=5
            )
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        color_formatter = colorlog.ColoredFormatter(
            "%(asctime)s %(log_color)s[%(levelname)s]  %(message)s",
            log_colors={
                "DEBUG": "reset",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
            secondary_log_colors={},
            style="%",
        )
        console_handler.setFormatter(color_formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
