import sys, logging

def getLogger():
    '''Get a standard logger for testing'''

    formatter = "%(asctime)s %(filename)s:%(lineno)d:%(levelname)s:%(message)s"

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(formatter))
    console_handler.setLevel(logging.INFO)

    logger = logging.getLogger("ecstest_logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger

logger = getLogger()

