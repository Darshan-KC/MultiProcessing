# Write a program to find cube and square using multiprocessing

import multiprocessing

def square(n,result):
    result.value = n*n

def cube(n,result):
    result.value = n*n*n

def main():
    square_result = multiprocessing.Value('i')
    cube_result = multiprocessing.Value('i')
    
    p1 = multiprocessing.Process(target=square,args=(4,square_result))
    p2 = multiprocessing.Process(target=cube,args=(2,cube_result))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Square: {square_result.value}")
    print(f"Cube: {cube_result.value}")

if __name__ == "__main__":
    main()