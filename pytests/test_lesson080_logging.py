import logging


def test_logging_demo():
    # __name__ gets the testcase name
    logger = logging.getLogger(__name__)

    # path where the file will be saved
    file_handler = logging.FileHandler('pytests\\logfile.log')

    # gives format to the printed message
    formatter = logging.Formatter(
        "%(asctime)s: %(levelname)s: %(name)s: %(message)s")

    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)

    # Settin a level will print only messages from that level and up
    logger.setLevel(logging.CRITICAL)

    logger.debug('A debug statement is printed')
    logger.info('An info statement is printed')
    logger.warning('Something is in warning mode')
    logger.error('A major error has happened')
    logger.critical('Critical issue')
