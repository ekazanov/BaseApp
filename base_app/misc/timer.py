#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
A short summary that makes sense on its own.

Long description.
args in main() are processed in accordance with setup tools requirements.
"""

from __future__ import print_function

__author__ = "Evgeny Kazanov"

import sys
import time

class Timer(object):
    """
    """

    def __init__(self, interval=None):
        """
        """
        self._prev_time = None
        self.interval = interval

    def check_timer(self):
        cur_time = time.time()
        if cur_time - self.interval >= self._prev_time:
            self._prev_time = cur_time
            return True
        else:
            return False

if __name__ == "__main__":
    TIMER_02S = Timer(interval=2.0)
    time_cnt = 0
    while True:
        time.sleep(1)
        time_cnt =+ 1
        print("cnt={}".format(time_cnt))
        if TIMER_02S.check_timer():
            print("timer_cnt = {}".format(time_cnt))
