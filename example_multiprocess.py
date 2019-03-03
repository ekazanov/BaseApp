#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Example for the BaseApp multiprocess application.
"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

from base_app.multiprocess.main import BaseAppMultiprocessMain
from base_app.multiprocess.worker import BaseAppMultiprocessWorker

class UserWorker(BaseAppMultiprocessWorker):

    def __init__(self, *args, **kwargs):
        super(UserWorker, self).__init__(*args, **kwargs)
        self.main_loop_sleep_time = 1

    def worker_action(self):
        print("UsersWorker: {}".format(self.name))
        return
        
main = BaseAppMultiprocessMain()
main.main_loop_sleep_time = 0.5
worker = UserWorker(name='Worker 01')
main.register_worker(worker=worker, check=False)
worker = UserWorker(name='Worker 02')
main.register_worker(worker=worker, check=False)
main.run()
