#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
"""

# TODO Add message handler to worker
# TODO Add message sending to worker

from __future__ import print_function

__author__ = "Evgeny Kazanov"

import sys

from base_app.multiprocess.main import Main
from base_app.multiprocess.worker import Worker

class UserWorker(Worker):

    def __init__(self, *args, **kwargs):
        super(UserWorker, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = 1

    def worker_action(self):
        print("UsersWorker: {}".format(self.name))
        return

class UserMain(Main):

    def main_action(self):
        print("UserMain.main_action()")
        return



main = UserMain()
main.main_loop_sleep_time = 0.5
worker = UserWorker(name='Worker 01')
main.register_worker(worker=worker)
worker = UserWorker(name='Worker 02')
main.register_worker(worker=worker)

print("main.msg_router.message_route_d = {}".format(main.msg_router.message_route_d))

sys.exit(0)

main.run()
