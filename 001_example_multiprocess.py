#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
The BaseApp multiprocess application example.

1. Create the application classes.

2. Run the classes.

3. Exit by the Ctrl-C.
"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

import time

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

print(__doc__)
time.sleep(1)

main = UserMain()
main.main_loop_sleep_time = 0.5
worker = UserWorker(name='Worker 01')
main.register_worker(worker=worker, check=False)
worker = UserWorker(name='Worker 02')
main.register_worker(worker=worker, check=False)
main.run()
