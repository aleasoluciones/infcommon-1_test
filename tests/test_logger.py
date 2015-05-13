# -*- coding: utf-8 -*-

import unittest
from doublex import *
from hamcrest import *

from infcommon import logger

IRRELEVANT_NAME = 'irrelevant_name'
IRRELEVANT_MESSAGE = 'irrelevant_message'
IRRELEVANT_INFO_MESSAGE = 'irrelevant_info_message'


class LoggerTest(unittest.TestCase):
    def setUp(self):
        self.stream = Spy()
        self.set_level(logger.ERROR)
        self.logger = logger.Logger(IRRELEVANT_NAME)

    def set_level(self, level):
        logger.configure(handlers={
                'fake_handler': {
                    'class': 'logging.StreamHandler',
                    'stream': self.stream
                }
            }, loggers={
                IRRELEVANT_NAME: {
                    'level': level,
                    'handlers': ['fake_handler']
                }
            }
        )

    def test_log_error(self):
        self.logger.error(IRRELEVANT_MESSAGE)

        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_MESSAGE)))

    def test_initialy_no_info_or_debug_output(self):
        self.logger.debug(IRRELEVANT_MESSAGE)
        self.logger.info(IRRELEVANT_INFO_MESSAGE)

        assert_that(self.stream.write, never(called().with_args(contains_string(IRRELEVANT_MESSAGE))))
        assert_that(self.stream.write, never(called().with_args(contains_string(IRRELEVANT_INFO_MESSAGE))))

    def test_debug_log_when_debug_level_selected(self):
        self.logger.set_level(logger.DEBUG)

        self.logger.debug(IRRELEVANT_MESSAGE)

        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_MESSAGE)))

    def test_info_and_debug_log_when_debug_level_selected(self):
        self.logger.set_level(logger.DEBUG)

        self.logger.debug(IRRELEVANT_MESSAGE)
        self.logger.info(IRRELEVANT_INFO_MESSAGE)

        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_MESSAGE)))
        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_INFO_MESSAGE)))

    def test_info_log_when_info_level_selected(self):
        self.logger.set_level(logger.INFO)

        self.logger.info(IRRELEVANT_MESSAGE)

        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_MESSAGE)))

    def test_no_debug_output_and_toggle_debug_shows_debug_output(self):
        self.logger.debug(IRRELEVANT_MESSAGE)
        assert_that(self.stream.write, never(called().with_args(contains_string(IRRELEVANT_MESSAGE))))

        logger.activate_debug()
        self.logger.debug(IRRELEVANT_MESSAGE)
        assert_that(self.stream.write, called().with_args(contains_string(IRRELEVANT_MESSAGE)))

        logger.deactivate_debug()
        self.logger.debug(IRRELEVANT_MESSAGE)

        assert_that(self.stream.write, called().times(1).with_args(contains_string(IRRELEVANT_MESSAGE)))
