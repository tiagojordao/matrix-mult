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
    childs = []
    if pid == 0: # verifica se é processo filho
        childs.append(os.getppid()) # cria uma lista com os filhos
        aux = [] # list que guarda a soma dos elementos
        for a,b in zip(row_a, row_b):
            aux.append(a + b)
        results.append(aux)
    else:
        for c in childs:
            os.waitpid(c, 0,0) # espera cada filho terminar a execução
        exit(0)

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

        threads[-1].join()
        
        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time

        with open('result_thread_sum.txt', 'a') as file:
            file.write(str(time_in_program.total_seconds())+"\n")

        #print_matrix(results)
    
    else: 
        for arg, rand in zip(matrix_a, matrix_b):
            func(arg, rand, results)

        #print_matrix(results)

        end_time = datetime.datetime.today()
        time_in_program = end_time - start_time

        with open('result_proc_sum.txt', 'a') as file:
            file.write(str(time_in_program.total_seconds())+"\n")

if __name__ == '__main__':
    res = []
    args = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
    vals = [1,2,3,4,5,6,8,10,20,30,40,50,75,100]
    for i in vals:
        r1 = random_matrix(i,i)
        r2 = random_matrix(i,i)
        args2 = [r1,r2]
        unroll(args2, sum_proc, 'proc', res)
    for i in vals:
        r1 = random_matrix(i,i)
        r2 = random_matrix(i,i)
        args2 = [r1,r2]
        unroll(args2, sum_thre, 'thre', res)