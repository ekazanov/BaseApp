"""
Project: BaseApp. Class: BaseAppMessageRouter.

TODO: Not tested.
"""

from multiprocessing import Queue
from Queue import Empty

class MessageReceiver(object):
    """
    Message format:
        ["<msg_type>", <msg_body>]

    Where:
        <msg_type> - String.
        <msg_body> - any valid Python type.
    """

    def __init__(self):
        self.message_handler_d = {}
        self.in_q = Queue()

    def register_handler(self, message_type=None, message_handler=None):
        self.message_handler_d[message_type] = message_handler
        return

    def route_message(self, message):
        self.message_handler_d[message["type"]](message["body"])
        return

    def _get_message(self):
        try:
            msg_type, msg_body = self.in_q.get(block=False)
        except Empty:
            return (None, None)
        return (msg_type, msg_body)
