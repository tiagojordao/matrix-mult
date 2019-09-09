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

def sum_proc(row_a, row_b, results):
    pid = os.fork() # cria um filho pra cada elemento da matriz
    if pid == 0: # verifica se é processo filho
        aux = [] # list que guarda a soma dos elementos
        for a,b in zip(row_a, row_b):
            aux.append(a + b)
        results.append(aux)
    else:
        os.wait()

def sum_thre(i, j, a, b, results):
    threading.currentThread() # executa a soma na thread atual
    results[i][j] = a + b

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results):
    start_time = datetime.datetime.today()
    file = open("result_sum.txt","w")
    matrix_a = args[0]
    matrix_b = args[1]

    if method == "thre":
        threads = []
        cols = len(matrix_a[0])
        rows = len(matrix_a)

        results = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(i, j, matrix_a[i][j], matrix_b[i][j], results))
                threads[-1].start()
                
        print_matrix(results)
    
    else: 
        for arg, rand in zip(matrix_a, matrix_b):
            func(arg, rand, results)
                      
        if len(results) == len(matrix_a):
            print_matrix(results)

if __name__ == '__main__':
    res = []
    args = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
    r1 = random_matrix(10,10)
    r2 = random_matrix(10,10)
    args2 = [r1,r2]
    unroll(args, sum_proc, 'proc', res)
    # unroll(args2, sum_thre, 'thre', res)
