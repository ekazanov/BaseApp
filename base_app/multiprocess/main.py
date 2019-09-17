#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Project: BaseApp. Class: BaseAppMain.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

import time

from message_receiver import MessageReceiver
from message_router import MessageRouter
from signal_utils import ExitSignalReceiver
from message_utils import send_message

class Main(object):

    def __init__(self, check_workers=False):
        self.main_loop_sleep_time = 0.01
        self.worker_arr = []
        self.worker_to_check_arr = []
        self.check_workers = check_workers
        self.msg_receiver = MessageReceiver()
        self.msg_router = MessageRouter()
        self.exit_signal_receiver = ExitSignalReceiver()
        self._exit_flag = False
        self.name = "main"
        self.msg_router.register_receiving_objets(receiving_object=self)

    def register_worker(self, worker=None):
        self.worker_arr.append(worker)
        worker.set_main_input_q(main_input_q=self.msg_receiver.in_q)
        worker.set_msg_router(self.msg_router)
        self.msg_router.register_receiving_objets(receiving_object=worker)
        if self.check_workers:
            self.worker_to_check_arr.append(worker)
        return

    def run(self):
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
            # Exit by signal
            if self.exit_signal_receiver.exit_flag:
                break
            # Exit by exit() call
            if self._exit_flag:
                break
            time.sleep(self.main_loop_sleep_time)
        self._exit_workers()
        for worker in self.worker_arr:
            worker.proc.join()
        return

    def _exit_workers(self):
        # send exit message to workers
        for worker in self.worker_arr:
            self.send_exit_msg(worker)
        return

    def send_exit_msg(self, worker):
        msg = ("exit", None)
        worker.msg_receiver.in_q.put(msg)
        return

    def exit(self):
        """Exit the application.
        """
        self._exit_flag = True
        return

if __name__ == "__main__":
    main = Main()
    main.run()
