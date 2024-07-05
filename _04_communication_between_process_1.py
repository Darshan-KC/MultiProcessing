# In multiprocessing, any newly created process will do following:

# run independently
# have their own memory space.
# Consider the program below to understand this concept:

import multiprocessing

result = []

def square_list(mylist):
    pass

if __name__ == "__main__":
    pass