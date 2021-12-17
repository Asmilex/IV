from asyncio.log import logger
import logging
import logging.handlers
import loguru
import sys

from vin.vin_config import VinConfig

class LoggerConfig:
    def get(config: VinConfig = None):
        if not config:
            config = VinConfig()

        logger = loguru.logger
        #self.logger = logging.getLogger("")
        logger = LoggerConfig.__setup_config__(logger, config)

        return logger

    def __setup_config__(logger, config: VinConfig):
        logger.remove()
        logger.level(config.log_level)

        logger.info(config.log_to_file)
        if config.log_to_file:
            logger.add(config.logfile, rotation = "500 MB")

        if config.log_to_console:
            logger.add(sys.stderr)

        return logger

logger = LoggerConfig.get()
