# -*- coding: utf-8 -*-

import unittest
from hamcrest import *
from doublex import *

import datetime

from infcommon import clock as clock_module

IRRELEVANT_TIME = datetime.datetime.now()
IRRELEVANT_SECONDS = 2
IRRELEVANT_SLEEP = datetime.timedelta(seconds=IRRELEVANT_SECONDS)


class SleeperTest(unittest.TestCase):

    def setUp(self):
        with Stub(clock_module.Clock) as self.clock:
            self.clock.now().returns(IRRELEVANT_TIME)
        self.time_module = Spy()
        self.sleeper = clock_module.Sleeper(self.clock, self.time_module)

    def test_sleep_until_time(self):
        self.sleeper.sleep_until(IRRELEVANT_TIME + IRRELEVANT_SLEEP)

        assert_that(self.time_module.sleep, called().with_args(
            IRRELEVANT_SECONDS))

    def test_dont_sleep_if_already_at_desired_time(self):
        self.sleeper.sleep_until(IRRELEVANT_TIME)

        assert_that(self.time_module.sleep, never(called()))

    def test_sleep(self):
        self.sleeper.sleep(IRRELEVANT_SECONDS)

        assert_that(self.time_module.sleep, called().with_args(IRRELEVANT_SECONDS))
