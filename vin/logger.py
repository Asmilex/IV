import loguru
import sys

from vin.vin_config import VinConfig

class LoggerConfig:
    def get(logger, config: VinConfig = None):
        if not config:
            config = VinConfig()

        logger = LoggerConfig.change_config(logger, config)

        return logger

    def change_config(logger, config: VinConfig):
        logger.remove()
        logger.level(config.log_level)

        logger.info(config.log_to_file)
        if config.log_to_file:
            logger.add(config.logfile, rotation = "500 MB")

        if config.log_to_console:
            logger.add(sys.stderr)

        return logger

logger = LoggerConfig.get(loguru.logger)
