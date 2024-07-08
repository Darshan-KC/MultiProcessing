# Queue : A simple way to communicate between process with multiprocessing is to use a Queue to pass messages back and forth. Any Python object can pass through a Queue.
# Note: The multiprocessing.Queue class is a near clone of queue.Queue.

import multiprocessing

def square_list(mylist,q):
    """ 
    function to square a given list 
    """
    # append squares of mylist to queue
    for num in mylist:
        q.put(num*num)
        
def print_queue(q):
    """ 
    function to print queue elements 
    """
    print("Queue elements:") 
    while not q.empty():
        print(q.get())
        
    print("Queue is now empty!")
    
def main():
    """
    Main function
    """
    mylist = [1,2,3,4]
    
    # Creating multiprocessing Queue
    q = multiprocessing.Queue()
    
    # Creating new process
    p1 = multiprocessing.Process(target=square_list,args=(mylist,q))
    p2 = multiprocessing.Process(target=print_queue,args=(q,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
    
if __name__ == "__main__":
    main()
    