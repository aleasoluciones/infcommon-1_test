# -*- coding: utf-8 -*-

import unittest
from hamcrest import *
from pyDoubles.framework import *

import datetime

from common import clock as clock_module


class ClockTest(unittest.TestCase):

    def test_today(self):
        date_obj = empty_spy()
        clock = clock_module.Clock(date_obj=date_obj)
        clock.today()
        assert_that_method(date_obj.today).was_called()

    def test_now(self):
        datetime_obj = empty_spy()
        clock = clock_module.Clock(datetime_obj=datetime_obj)
        clock.now()
        assert_that_method(datetime_obj.now).was_called()

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
