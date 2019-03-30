#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
The BaseApp multiprocess application example.
"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

from base_app.multiprocess.main import Main
from base_app.multiprocess.worker import Worker

class UserWorker(Worker):

    def __init__(self, *args, **kwargs):
        super(UserWorker, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = 1

    def worker_action(self):
        print("UsersWorker: {}".format(self.name))
        return
        
main = Main()
main.main_loop_sleep_time = 0.5
worker = UserWorker(name='Worker 01')
main.register_worker(worker=worker, check=False)
worker = UserWorker(name='Worker 02')
main.register_worker(worker=worker, check=False)
main.run()
