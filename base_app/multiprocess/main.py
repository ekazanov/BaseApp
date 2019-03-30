#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Project: BaseApp. Class: BaseAppMain.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

import time

from message_receiver import MessageReceiver


class Main(object):

    def __init__(self):
        self.main_loop_sleep_time = 0.01
        self.worker_arr = []
        self.worker_to_check_arr = []
        self.msg_receiver = MessageReceiver()

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

    def main_action(self):
        msg = "Unimplemented method: {}".format(str(self.__class__)+'.'+str(__name__))
        raise Exception(msg)

    def _main_loop(self):
        while True:
            self.main_action()
            time.sleep(self.main_loop_sleep_time)
        return

    def exit(self):
        # send exit message to workers
        for worker in self.worker_arr:
            self.send_exit_msg(worker)
        return

    def send_exit_msg(self, worker):
        msg = ("exit", None)
        worker.msg_receiver.in_q.put(msg)
        return
    
if __name__ == "__main__":
    main = Main()
    main.run()
