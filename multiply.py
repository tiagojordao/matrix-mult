import os
import random
import threading
import datetime

def process_multiply(row_a, row_b, results):
    pid = os.fork()
    if pid == 0:
        aux = []
        for a, b in zip(row_a, row_b):
            aux.append(a + b)
        results.append(aux)
    else:
        os.wait()

def thre_multiply(i, j, a, b, results):
    threading.currentThread()
    aux = 0
    for idx in range(len(a)):
        aux += a[idx] * b[idx]
    results[i][j] = aux 

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results):
    matrix_a = args[0]
    matrix_b = args[1]

    start_time = datetime.datetime.today()

    if method == "thre":
        threads = []
        cols = len(matrix_b[0])
        rows = len(matrix_b)

        results = [[0 for i in range(cols)] for j in range(len(matrix_b))]

        for j in range(cols):
            aux = []
            for i in range(rows):
                aux.append(matrix_b[i][j])
            for idx, arg in enumerate(matrix_a):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(idx, j, arg, aux, results))
                threads[-1].start() 

        file = open("result_thread_multiply.txt","w") 
        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time
        file.write(str(time_in_program.total_seconds())+"\n")
        file.close()
        print_matrix(results)
    
    else:
        for arg1, arg2 in zip(matrix_a, matrix_b):
            func(arg1, arg2, results)

        file = open("result_proc_multiply.txt","w") 
        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time
        file.write(str(time_in_program.total_seconds())+"\n")
        file.close()
        if len(results) == len(matrix_a):
            print_matrix(results)

if __name__ == '__main__':
    res = []
    args = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
    unroll(args, process_multiply, 'proc', res)
    # unroll(args, thre_multiply, 'thre', res)
