"""
Project: BaseApp. Class: BaseAppMain.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

from multiprocessing import Process
import time

from message_receiver import MessageReceiver

class Worker(object):

    def __init__(self, name=None, main_input_q=None):
        self.main_loop_sleep_time = 0.01
        self.proc = None
        self.name = name
        self.msg_receiver = MessageReceiver()
        self.main_input_q = main_input_q
        
    def run_worker(self):
        print("BaseAppMultiprocessWorker.run_worker()")
        self.proc = Process(target=self._main_loop)
        self.proc.start()
        return self.proc

    def worker_action(self):
        msg = "Unimplemented method: {}".format(self.__class__+'.'+__name__)
        raise Exception(msg)
   
    def _main_loop(self):
        while True:
            self.worker_action()
            time.sleep(self.main_loop_sleep_time)
        return
