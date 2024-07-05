# In multiprocessing, any newly created process will do following:

# run independently
# have their own memory space.
# Consider the program below to understand this concept:

import multiprocessing

result = []

def square_list(mylist :list) ->None:
    """ 
    function to square a given list 
    """
    result = [x*x for x in mylist]
    
    print("Result (in process p1): {}".format(result))

if __name__ == "__main__":
    # input list 
    mylist = [1,2,3,4]
    
    # Creating new process
    p1 = multiprocessing.Process(target=square_list,args=(mylist,))
    
    p1.start()
    
    p1.join()    

    # print global result list 
    print("Result(in main program): {}".format(result))