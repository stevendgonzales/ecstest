#!/usr/bin/env python

import os, sys
from testtools import TestCase
import logger

LOG = logger.getLogger()

class LogTest(TestCase):
    def setUp(self):
        super(LogTest, self).setUp()

    def test_log_message(self):
        LOG.info("This is an information message")
        LOG.error("This is an error message")
        LOG.debug("This is a debug message")

