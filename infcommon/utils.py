# -*- coding: utf-8 -*-

import time
import datetime
import logging

MIN_SLEEP_TIME = 0.2
MAX_RECONNECTION_TIME = 10
SUCESSFUL_RECONNECTION_TIME = 1


def do_stuff_with_exponential_backoff(exceptions, stuff_func, *args, **kwargs):

    def _sleep_for_reconnect(try_num):
        reconnect_sleep_time = min(MAX_RECONNECTION_TIME, (try_num**2)*MIN_SLEEP_TIME)
        logging.info("Waiting for reconnect try {} sleeping {}s".format(try_num, reconnect_sleep_time))
        time.sleep(reconnect_sleep_time)

    try_num = 1
    while True:
        try:
            t1 = datetime.datetime.now()
            return stuff_func(*args, **kwargs)
        except exceptions:
            logging.error("Error performing stuff", exc_info=True)
            if datetime.datetime.now() - t1 > datetime.timedelta(seconds=SUCESSFUL_RECONNECTION_TIME):
                try_num = 1
            else:
                try_num += 1
            _sleep_for_reconnect(try_num)
