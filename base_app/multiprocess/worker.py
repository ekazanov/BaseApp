"""
Project: BaseApp. Class: Worker.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

from multiprocessing import Process
import time

from signal_utils import ignore_sigint
from message_receiver import MessageReceiver

class Worker(object):

    def __init__(self, name=None):
        self.main_loop_sleep_time = 0.01
        self.proc = None
        self.name = name
        self.main_input_q = None
        self.msg_receiver = MessageReceiver()
        self._exit_flag = False
        self.msg_receiver.register_handler(message_type="exit",
                                           message_handler=self._exit)

    def set_main_input_q(self, main_input_q=None):
        self.main_input_q = main_input_q
        return

    def run_worker(self):
        self.proc = Process(target=self._main_loop)
        self.proc.start()
        return self.proc

    def worker_action(self):
        msg = "Unimplemented method: {}".format(self.__class__+'.'+__name__)
        raise Exception(msg)

    def _main_loop(self):
        ignore_sigint()
        while not self._exit_flag:
            self.worker_action()
            self.msg_receiver.get_messages()
            time.sleep(self.main_loop_sleep_time)
        return

    def _exit(self, msg_data):
        self._exit_flag = True
        return
