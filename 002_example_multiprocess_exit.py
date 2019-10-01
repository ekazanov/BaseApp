#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
The BaseApp multiprocess application example.
Exit by the using Main.exit() method.

1. Create the Main/worker classes.

2. Run a separate thread for the exit call.

3. sleep(2) and call exit()

4. The appliaction has to exit.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

import time
import threading

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
main.register_worker(worker=worker)
worker = UserWorker(name='Worker 02')
main.register_worker(worker=worker)

main_thread = threading.Thread(target=main.run)
main_thread.start()
print("--------------------> main() started")
time.sleep(2)
print("--------------------> Send exit messages")
main.exit()
