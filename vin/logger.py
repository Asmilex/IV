import loguru
import sys

from vin.vin_config import VinConfig


# ────────────────────────────────────────────────────────────────────────────────

class __Borg__:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# ────────────────────────────────────────────────────────────────────────────────

class LoggerConfig(__Borg__):
    def __init__(self, config: VinConfig = None):
        __Borg__.__init__(self)
        self.logger = loguru.logger

        if not config:
            config = VinConfig()

        self.__change_config__(config)


    def __change_config__(self, config: VinConfig):
        self.logger.remove()
        self.logger.level(config.log_level)

        self.logger.info(config.log_to_file)
        if config.log_to_file:
            self.logger.add(config.logfile, rotation = "500 MB")

        if config.log_to_console:
            self.logger.add(sys.stderr)


    @staticmethod
    def get(config: VinConfig = None):
        if not config:
            config = VinConfig()

        obj = LoggerConfig()
        obj.__change_config__(config)

        return obj.logger