"""
Project: BaseApp. Class: MessageRouter.
"""
from multiprocessing import Queue
try:
    # Python2
    from Queue import Empty
except ModuleNotFoundError:
    # Python3
    from queue import Empty


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

    def get_messages(self):
        while True:
            msg_type, msg_body = self._get_message()
            if (msg_type, msg_body) == (None, None):
                break
            # Execute message handler
            self.message_handler_d[msg_type](msg_body)
        return
