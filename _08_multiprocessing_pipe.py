# Pipes : A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required.
# multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others).

import multiprocessing

