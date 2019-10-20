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
    * It allows use few frameworks with event loops in separate processes.

# Features #

The multiprocessing module allows to develop following architectures:

    * The main process and the number of the different workers. 
      Main process and workers can send messages to each other.
    * The main process and the number of the identical workers. 
      The workers take tasks from the task queue and work on tasks.

# Usage #

