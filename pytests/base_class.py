import logging
import inspect


class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('pytests\\logfile.log')

        formatter = logging.Formatter(
            "%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        return logger
