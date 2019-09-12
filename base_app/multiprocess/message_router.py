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

    def register_receiving_objetc(self, receiving_object=None):
        self.message_route_d[receiving_object.name] = receiving_object
        return

    def route_message_to_receiver(self,
                                  receiving_object_name=None,
                                  message=None ):
        # Send message to receiving_object
        receiving_obj = self.message_route_d[receiving_object_name]
        receiving_obj.msg_receiver.in_q.put(message)
        return
