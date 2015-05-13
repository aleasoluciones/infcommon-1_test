# -*- coding: utf-8 -*-

import unittest
from hamcrest import *
from doublex import *

import datetime

from infcommon import clock as clock_module


class ClockTest(unittest.TestCase):

    def test_today(self):
        date_obj = Spy()
        clock = clock_module.Clock(date_obj=date_obj)
        clock.today()
        assert_that(date_obj.today, called())

    def test_now(self):
        datetime_obj = Spy()
        clock = clock_module.Clock(datetime_obj=datetime_obj)
        clock.now()
        assert_that(datetime_obj.now, called())

    def test_utctimestampnow(self):
        now = clock_module.Clock().now()
        utc_timestamp = clock_module.Clock().utctimestampnow()
        local_from_timestamp = clock_module.Clock.fromtimestamp(utc_timestamp)
        self.assertTrue(clock_module.Clock.aprox(now, local_from_timestamp))

    def test_timestamp(self):
        # This conversion loose some microseconds so we only check if the
        # conversion is approximately correct
        now = datetime.datetime.now()
        ts = clock_module.Clock.timestamp(now)
        now_from_ts = clock_module.Clock.fromtimestamp(ts)
        self.assertTrue(clock_module.Clock.aprox(now, now_from_ts))
