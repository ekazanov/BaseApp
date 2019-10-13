"""
Project: BaseApp. Class: TaskQueue.

TODO: Add a Queue attribute.
TODO: Add a TaskQueue.get_task() method.
TODO: Add a Worker.task_queue attribute
TODO: Design the rest of the task_queue processing.
"""

from multiprocessing import Queue
try:
    # Python2
    from Queue import Empty
except ModuleNotFoundError:
    # Python3
    from queue import Empty

class TaskQueue(object):
    """
    """

    def __init__(self, ):
        """
        """
        pass
