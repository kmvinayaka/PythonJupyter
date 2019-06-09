import multiprocessing
import time 
def calc_square(number):
    print('Square:' , number * number)
    result = number * number
    print(result)
def calc_quad(number):
    print('Quad:' , number * number * number * number)
if __name__ == "__main__":
    ts = time.time()
    number = 7
    #result = None
    p1 = multiprocessing.Process(target=calc_square, args=(number,))
    print(p1)
    p2 = multiprocessing.Process(target=calc_quad, args=(number,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    te = time.time()
    print(te - ts)
    
                        
    
