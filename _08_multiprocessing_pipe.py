# Pipes : A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required.
# multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others).

import multiprocessing

def sender(conn, msgs):
    """
    function to send messages to other end of pipe
    """
    
    for msg in msgs:
        conn.send(msg)
        print("Send the message {}".format(msg))
    conn.close()
    
def receiver(conn):
    """
    function to print the message received from other end of pipe
    """
    
    while True:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message : {}".format(msg))
        
def main() -> None:
    """
    Main function
    """
    # messages to be sent 
    msgs = ["Namaste", "hey", "hru?", "END"]
    
    # Create a pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    
    #create new processes
    p1 = multiprocessing.Process(target=sender,args=(parent_conn,msgs))
    p2 = multiprocessing.Process(target=receiver,args=(child_conn,))
    
    p1.start()
    p1.join()

    p2.start()
    p2.join()
    
if __name__ == "__main__":
    main()