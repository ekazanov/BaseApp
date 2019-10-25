BaseApp
=======

# Info #

Author: Evgeny Kazanov

# Introduction #

The BaseApp is a simple library/framework.

The main goal of it is to provide a set of tools for python
application creating.

Probably in the future it will contain different modules. At the
moment the multiprocessing module is nearly ready.

It can be useful to create the Python multiprocessing applications. The
such applications have the following advantages:

    * The good multiprocessing application is much more reliable.
    * It reduces application complexity.
    * It resolves the famous GIL problem.
    * It allows to use few frameworks with event loops in the separate processes.

# Features #

The multiprocessing module allows to develop following architectures:

    * The main process and the number of the different workers.
      Main process and workers can send messages to each other.
    * The main process and the number of the identical workers.
      The workers take tasks from the task queue and work on tasks.

# Internals #

## Application structure ##

  * Develop the UserMain (One can use other class name of course)
    class which inherits from Main class.
    * Develop the UserMain.main_action() method.
    * Develop message handlers in UserMain. They are called for each
      message arriving to UserMain process.
    * Register the message handlers in `UserMain.__init__()`
  * Develop the UserWorker (the class name can vary) classes which
    inherit from Worker class.
    * Develop the UserWorker.worker_action() method.
    * Develop message handlers in UserWorker. They are called for each
      message arriving to UserWorker process.
    * Register the message handlers in `UserWorker.__init__()`
  * Create and main object, create and register worker objects:
    *   `main = UserMain()`
    *   `worker = UserWorker01(name='Worker_01')`
    *   `main.register_worker(worker=worker)`
    *   `worker = UserWorker01(name='Worker_02')`
    *   `main.register_worker(worker=worker)`
  * Start main process:
    * `main.run()`

## Main process life cycle ##

  After the start (`main.run()` call):

  1. The `main._run_workers()` method is called. It starts the worker
     processes.
  2. The `main._main_loop_workers()` method is called. In the loop:
    1. The `main._main_action()` method is called. It is defined in
       UserMain class. The Main background actions happen here.
    2. The `main.msg_receiver.get_messages()` method is called. It
       receives messages if there are any. For every message the
       message handler is called.
    3. The exit flag is processed. If it is true exit from the loop.
  3. Call `self._exit_workers()` It sends exit message to the workers.
  4. Wait when all workers are finished.
  5. Exit.

## Worker process life cycle ##

  **Note:** In this section the classes are reffered as:

  - `Worker` - `base_app.multiprocess.worker.Worker` class
  - `UserWorker` - The developer's worker class which inherits from
    the `base_app.multiprocess.worker.Worker` class.

  **Life cycle:**

  1. In the `User.__init__()` method the message handlers are
     registered.
  2. The `User.run_worker()` starts the worker process. The worker
     process runs as an User._main_loop() method. In it:
    1. Call UserWorker.worker_action():
        - (Optional) If the application is designed as a *task queue
           application* get task from task queue (See
           004_example_task_queue.py). Do task.
        -  If the application is not designed as a *task queue
           application* the background worker work happends here.
    2. Get messages and call message handlers.
    3. Check Worker._exit_flag
    4. return - exit from the worker process.

### Blocking/non blocking mode ###

To be developed and written.

## Messaging ##

### Object message ###

Message is the python tuple:

`(<message type>, <message body>)`


Message should be send using the `MessageRouter.send_message()` method
like this:

```python
self.msg_router.send_message(
   receiving_object_name="<object_name>",
   message_type="<message type>",
   message_body=<message body>)
```

Where:

 - `<object_name>` - Receiving object name attribute
   (str). `receiving_object.name`
 - `<message type>` - Sring with message type. The message type is
   used as a key for message handler call.
 - `<message body>` - Any python object which can be pickled.

### Task message ###

The task message type can be the any pickleable python type.

Task message is sent using the `TaskQueue.send_task()` method like
following:

```python
self.msg_router.task_queue.send_task(<task message object>)
```

### Message routing ###

#### Object messages ####

Every worker process and main process has an 

Object messages are sent to the corresponded object input 

#### Task messages ####

#### Exit messages ####

### Message handlers ###


# Usage #

## Class development ##

One should develop Main class and Worker classes.
