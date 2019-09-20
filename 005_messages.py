#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
"""

# TODO Add message handler to worker
# TODO Add message sending to worker
# Add message handler to UserWorker
# Add message handler to UserMain

from __future__ import print_function

__author__ = "Evgeny Kazanov"

import sys

from base_app.multiprocess.main import Main
from base_app.multiprocess.worker import Worker

class UserWorker01(Worker):

    def __init__(self, *args, **kwargs):
        super(UserWorker01, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = 1
        self.msg_receiver.register_handler(
            message_type="print",
            message_handler=self._msg_handl_print_msg)

    def worker_action(self):
        print("UsersWorker: {}".format(self.name))
        return

    def _msg_handl_print_msg(self, msg_body=None):
        print("Worker: {}. Message: {}".format(self.name, msg_body))
        return

class UserWorker02(Worker):

    def __init__(self, *args, **kwargs):
        super(UserWorker02, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = 1
        self.msg_receiver.register_handler(
            message_type="print",
            message_handler=self._msg_handl_print_msg)

    def worker_action(self):
        print("UsersWorker: {}".format(self.name))
        return

    def _msg_handl_print_msg(self, msg_body=None):
        print("Worker: {}. Message: {}".format(self.name, msg_body))
        return

class UserMain(Main):

    def main_action(self):
        print("UserMain.main_action()")
        self._send_msg_to_worker_01()
        return

    def _send_msg_to_worker_01(self):
        self.msg_router.send_message(receiving_object_name="Worker_01",
                                     message_type="print",
                                     message_body="Message from Main to Worker_01")
        return

main = UserMain()
main.main_loop_sleep_time = 0.5
worker = UserWorker01(name='Worker_01')
main.register_worker(worker=worker)
worker = UserWorker02(name='Worker_02')
main.register_worker(worker=worker)

print("main.msg_router.message_route_d = {}".format(main.msg_router.message_route_d))

#sys.exit(0)

main.run()
