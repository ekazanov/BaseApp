# -*- coding: utf-8 -*-
"""
Project: BaseApp. Class: BaseAppMain.

"""
from __future__ import print_function

__author__ = "Evgeny Kazanov"

def send_message(receiver_class=None, msg_type=None, body=None):
    receiver_class.in_q.put({msg_type: body})
    return
