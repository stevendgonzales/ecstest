#!/usr/bin/env python

import os, sys, logging

def getLogger():
    '''Get a standard logger for testing'''

    formatter = "%(asctime)s %(filename)s:%(lineno)d:%(levelname)s:%(message)s"

    #logfile = os.environ['TEST_LOGFILE']
    #file_handler = logging.FileHandler(logfile)
    #file_handler.setFormatter(logging.Formatter(formatter))
    #file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(formatter))
    console_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    #logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

