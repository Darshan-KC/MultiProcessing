# multiprocessing module provides Array and Value objects to share data between processes.
# 1. Array: a ctypes array allocated from shared memory.
# 2. Value: a ctypes object allocated from shared memory.
# Given below is a simple example showing use of Array and Value for sharing data between processes.

import multiprocessing

def square_list(mylist, result, square_sum):
    """ 
    function to square a given list 
    arg: mylist -> list, result -> square of list, square_sum -> sum of square of list
    """
    for idx,num in enumerate(mylist):
        result[idx] = num*num
        
    square_sum.value = sum(result)
    
    # print result Array 
    print("Result(in process p1): {}".format(result[:])) 
  
    # print square_sum Value 
    print("Sum of squares(in process p1): {}".format(square_sum.value)) 

def main() ->None:
    """
    This is main function
    """
    mylist = [1,2,3,4]
    
    # Creating array of int datatypes with space for 4 integers
    result = multiprocessing.Array('i',4)
    
    # Creating Value of int data type
    square_sum = multiprocessing.Value('i') # you can use 'd' for float (double)
    
    p1 = multiprocessing.Process(target=square_list,args=(mylist,result,square_sum))

    p1.start()
    
    p1.join()

    # print result array 
    print("Result(in main program): {}".format(result[:])) 
  
    # print square_sum Value 
    print("Sum of squares(in main program): {}".format(square_sum.value))

if __name__ == "__main__":
    main()