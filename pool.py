import multiprocessing
import time
def square(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    inputs = [0,1,2,3,4]
    outputs = pool.map(square, inputs)
    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))