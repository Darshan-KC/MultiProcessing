# Server process : Whenever a python program starts, a server process is also started. From there on, whenever a new process is needed, the parent process connects to the server and requests it to fork a new process.
# A server process can hold Python objects and allows other processes to manipulate them using proxies.
# multiprocessing module provides a Manager class which controls a server process. Hence, managers provide a way to create data that can be shared between different processes.
# Server process managers are more flexible than using shared memory objects because they can be made to support arbitrary object types like lists, dictionaries, Queue, Value, Array, etc. Also, a single manager can be shared by processes on different computers over a network. They are, however, slower than using shared memory.

import multiprocessing

def print_record(records) ->None:
    """
    Record to print the records
    """
    for record in records:
        print("Name :{}\t Score : {}".format(record[0],record[1]))
        
def add_record(data,records) -> None:
    """
    
    """
        
    