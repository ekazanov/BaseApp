#! /usr/bin/python
# -*- coding: utf-8 -*-
"""The BaseApp multiprocess application example.
Exit by signal.

1. Create a run_base_app_mutiprocess_app() function which runs a main
process and two workers.

2.1. Start a run_base_app_mutiprocess_app() function as a separate process.
2.2. After 2 seconds send SIGINT signal to the process.
2.3. The process has to exit.

3.1. Start a run_base_app_mutiprocess_app() function as a separate process.
3.2. After 2 seconds send SIGTERM signal to the proceses.
3.3. The application process has to exit.
"""

from __future__ import print_function

__author__ = "Evgeny Kazanov"

import os
import signal
import time
from multiprocessing import Process

from base_app.multiprocess.main import Main
from base_app.multiprocess.worker import Worker

def run_base_app_mutiprocess_app():

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

    main.run()
    return

print(__doc__)
time.sleep(1)

print("Start Main() process for the SIGINT testing.")
MAIN_PROCESS = Process(target=run_base_app_mutiprocess_app)
MAIN_PROCESS.start()
MAIN_PROCESS_PID = MAIN_PROCESS.pid
print("MAIN_PROCESS_PID = {}".format(MAIN_PROCESS_PID))

time.sleep(2)
print("Send SIGINT signal to main process. PID={}".format(MAIN_PROCESS_PID))
os.kill(MAIN_PROCESS_PID, signal.SIGINT)

print("Start Main() process for the SIGTERM testing.")
MAIN_PROCESS = Process(target=run_base_app_mutiprocess_app)
MAIN_PROCESS.start()
MAIN_PROCESS_PID = MAIN_PROCESS.pid
print("MAIN_PROCESS_PID = {}".format(MAIN_PROCESS_PID))

time.sleep(2)
print("Send SIGTERM signal to main process. PID={}".format(MAIN_PROCESS_PID))
os.kill(MAIN_PROCESS_PID, signal.SIGTERM)
