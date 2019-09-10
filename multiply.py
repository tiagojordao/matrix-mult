import os
import random
import threading
import datetime

def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0,10)
    return matrix

def process_multiply(row_a, col_b, i, j, results):
    pid = os.fork()
    childs = []
    if pid == 0:
        aux = 0
        for k in range(len(row_a)):
            childs.append(os.getppid())
            aux += row_a[k] * col_b[k]
        results[i][j] = aux
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
        
        threads[-1].join()

        print_matrix(results)

        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time

        with open('result_thread_multiply.txt', 'a') as file:
            file.write(str(time_in_program.total_seconds())+"\n")
    
    else:
        cols = len(matrix_a[0])
        rows = len(matrix_a)

        cols2 = len(matrix_b[0])
        rows2 = len(matrix_b)

        results = [[0 for i in range(cols)] for j in range(len(matrix_b))]

        for j in range(cols2):
            aux = []
            for i in range(rows2):
                aux.append(matrix_b[i][j])
            for index, arg in enumerate(matrix_a):
                func(arg, aux , index, j, results)

        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time
        
        print_matrix(results)

        with open('result_proc_multiply.txt', 'a') as file:
            file.write(str(time_in_program.total_seconds())+"\n")
           

if __name__ == '__main__':
    res = []
    args = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
    vals = [1,2,3,4,5,6,8,10,20,30,40,50,75,100]
    for i in vals:
        r1 = random_matrix(i,i)
        r2 = random_matrix(i,i)
        args2 = [r1,r2]
        unroll(args2,process_multiply, 'proc', res)
    for i in vals:
        r1 = random_matrix(i,i)
        r2 = random_matrix(i,i)
        args2 = [r1,r2]
        unroll(args2,thre_multiply, 'thre', res)
