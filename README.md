BaseApp
=======

# Info #

Author: Evgeny Kazanov

# Introduction #

The BaseApp is a simple library/framework. The

The main goal of it is to provide a set of tools for python
application creating.

Probably in the future it will contain different modules. At the
moment the multiprocessing module is nearly ready.

# Features #

  * Main process.
  * Worker processes.
  * Messaging system.
  * Signal processing.

# Classes #

  * multiprocess.main.Main
  * multiprocess.worker.Worker
  * multiprocess.message_router.MessageRouter
  * multiprocess.signal_utils.ExitSignalReceiver
  * multiprocess.message_receiver.MessageReceiver

# Usage #

See 004_example_messages.py file.

## Define UserWorker classes ##

  * Develop a worker_action() method.
  * Develop a message handling methods (Optional).
  * Develop an __init__() method.
    * Register message handling methods.

## Define UserMain class ##

  * Develop a main_action() method.
  * Develop a message handling methods (Optional).
  * Develop an __init__() method.
    * Register message handling methods.

## Create and start objects ##

  * Create a main object.
  * Create the worker objects.
  * Register workers.
  * Call the run() method of the main object.
