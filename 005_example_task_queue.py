#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
The BaseApp multiprocess application example.

Exit using Ctrl-C.
"""

from __future__ import print_function

__author__ = "Evgeny Kazanov"

import os
import sys
import time

from base_app.multiprocess.main import Main
from base_app.multiprocess.worker import Worker
from base_app.misc.timer import Timer

class UserWorker(Worker):

    def __init__(self, *args, **kwargs):
        super(UserWorker, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = .1
        
    def worker_action(self):
        task = self.task_queue.get_task()
        if task is None:
            return None
        result = self.do_task(task[0], task[1])
        print("Worker_name={}, a = {}, b = {}, result = {}".format(
            self.name, result, task[0], task[1]))
        return True

    def do_task(self, a, b):
        result = a * b
        return result

class UserMain(Main):

    def __init__(self, *args, **kwargs):
        self.timer_1 = Timer(interval=1)
        self.sec_cnt = 0
        self.timer_2 = Timer(interval=2)
        self.timer_3_5 = Timer(interval=3.5)
        super(UserMain, self).__init__(*args, **kwargs)

    def main_action(self):
        
        return



print(__doc__)
time.sleep(1)

main = UserMain(task_queue=True)
main.main_loop_sleep_time = 0.1
worker = UserWorker(name='Worker_01')
main.register_worker(worker=worker)
worker = UserWorker(name='Worker_02')
main.register_worker(worker=worker)
worker = UserWorker(name='Worker_03')
main.register_worker(worker=worker)



main.run()

sys.exit(0)
