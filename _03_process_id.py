# Write a python program that print the ID of the processes running the target functions

import multiprocessing.process
import os
import multiprocessing

def worker1() -> None:
    print("ID of process running worker1 is : {}".format(os.getpid()))

def worker2() -> None:
    print("ID of process running worker2 is : {}".format(os.getpid()))

def main():
    # Printing main program process ID
    print("ID of main process: {}".format(os.getpid()))
    
    # creating processes 
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # Start the processes
    p1.start()
    p2.start()
    
    # Join the processes
    p1.join()
    p2.join()
    
    # both processes finished 
    print("Both processes finished execution!") 
    
    # check if processes are alive 
    print("Process p1 is alive: {}".format(p1.is_alive())) 
    print("Process p2 is alive: {}".format(p2.is_alive()))
    
if __name__ == "__main__":
    main()