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
    * Register the message handlers in UserMain.__init__()
  * Develop the UserWorker (the class name can vary) classes which
    inherit from Worker class.
    * Develop the UserWorker.worker_action() method.
    * Develop message handlers in UserWorker. They are called for each
      message arriving to UserWorker process.
    * Register the message handlers in UserWorker.__init__()
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

## Worker process Life cycle ##

### Blocking/non blocking mode ###

## Messaging ##

### Message formats ###

### Message sending ###

### Message routing ###

### Message handlers ###

=======
    1) The main process and the number of the different workers.
      Main process and workers can send messages to each other.
    2) The main process and the number of the identical workers.
      The workers take tasks from the task queue and work on tasks.

# Usage #

## Class development ##