# -*- coding: utf-8 -*-
"""
Project: BaseApp. Class: BaseAppMain.

TODO: remove this function and file.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

def send_message(receiver_class=None, msg_type=None, body=None):
    receiver_class.in_q.put({msg_type: body})
    return
