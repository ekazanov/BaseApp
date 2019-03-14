"""
Project: BaseApp. Class: BaseAppMain.

"""

class BaseAppMessageRouter(object):

    def __init__(self):
        self.message_handler_d = {}

    def register_handler(self, message_type=None, message_handler=None):
        self.message_handler_d[message_type] = message_handler
        return

    def route_message(self, message):
        self.message_handler_d[message["type"]]()
        return
