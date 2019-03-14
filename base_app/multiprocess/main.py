#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Project: BaseApp. Class: BaseAppMain.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

import time

from multiprocessing import Queue

class BaseAppMultiprocessMain(object):

    def __init__(self):
        self.main_loop_sleep_time = 0.01
        self.worker_arr = []
        self.worker_to_check_arr = []
        self.input_q = Queue()

    def register_worker(self, worker=None, check=False):
        self.worker_arr.append(worker)
        if check:
            self.worker_to_check_arr.append(worker)
        return
        
    def run(self):
        print("Hello world")
        self._run_workers()
        self._main_loop()
        return

    def _run_workers(self):
        for worker in self.worker_arr:
            worker.run_worker()
        return

    def _main_loop(self):
        while True:
            print("BaseAppMultiprocessMain._main_loop()")
            time.sleep(self.main_loop_sleep_time)
        return

    
if __name__ == "__main__":
    main = BaseAppMultiprocessMain()
    main.run()
