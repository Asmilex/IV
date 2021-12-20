import logging
import logging.handlers
import sys

from vin.vin_config import VinConfig


class Logger:
    def __init__(self, config: VinConfig = None):
        if not config:
            config = VinConfig.load()

        self.logger = logging.getLogger("")
        self.__setup_config__(config)

    def debug(self, text):
        return self.logger.debug(text)

    def info(self, text):
        return self.logger.info(text)

    def warning(self, text):
        return self.logger.warning(text)

    def error(self, text):
        return self.logger.error(text)

    def critical(self, text):
        return self.logger.critical(text)


    def __setup_config__(self, config):
        self.logger.setLevel(config['logging']['level'])

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Quitar el handler por defecto que viene
        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]

        if config['logging']['log_to_file']:
            file_handler = logging.handlers.RotatingFileHandler(
                config['logging']['logfile'], maxBytes=(300000), backupCount=3
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        if config['logging']['log_to_console']:
            console_handler = logging.StreamHandler(sys.stderr)
            console_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
