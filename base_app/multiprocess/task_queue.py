"""
Project: BaseApp. Class: TaskQueue.

DONE: Add a Queue attribute.
TODO: Add a TaskQueue.get_task() method.
TODO: Add a Worker.task_queue attribute.
TODO: Add a Main.task_queue attribute.
TODO: Add a task_queue argument to Main.__init_().
 - task_queue=False.
TODO: Add Worker.task_queue setting in Main.register_worker.
 - if task_queue==True set Main.task_queue = TaskQueue().
 - if task_queue==True set Worker.task_queue attribute.
TODO: Add TaskQueue section to READMR
TODO: Add an example for the TaskQueue.
TODO: Task should be sent to TaskQueue using MessageRouter.
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
        self.task_queue = Queue()

