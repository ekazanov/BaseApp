"""
Project: BaseApp. Class: MessageRouter.

TODO: Add example, test it.
"""


class MessageRouter(object):
    """
    Message format:
        ["<msg_type>", <msg_body>]

    Where:
        <msg_type> - String.
        <msg_body> - any valid Python type.
    """

    def __init__(self):
        self.message_route_d = {}
        """
        Routing dictionary.
        Format:
        {<receiving_object_name>: <receiving_object>}
        """

    def register_receiving_objets(self, receiving_object=None):
        self.message_route_d[receiving_object.name] = receiving_object
        return

    def send_message(self,
                     receiving_object_name=None,
                     message_type=None,
                     message_body=None):
        # Send message to receiving_object
        receiving_obj = self.message_route_d[receiving_object_name]
        message = (message_type, message_body)
        receiving_obj.msg_receiver.in_q.put(message)
        return
