import os
import random
import threading

def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0, 9)
    return matrix

def sum_proc(row_a, row_b, results):
    pid = os.fork() # cria um filho pra cada elemento da matriz
    if pid == 0: # verifica se é processo filho
        aux = [] # list que guarda a soma dos elementos
        for a,b in zip(row_a, row_b):
            aux.append(a + b)

        results.append(aux)  

def sum_thre(i, j, a, b, results):
    threading.currentThread() # executa a soma na thread atual
    results[i][j] = a + b

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def unroll(args, func, method, results):
    random_m = random_matrix(len(args), len(args[0]))

    if method == "thre":
        threads = []
        cols = len(args[0])
        rows = len(args)

        results = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(i, j, args[i][j], random_m[i][j], results))
                threads[-1].start()
                
        print_matrix(results)
    
    else: 
        for arg, rand in zip(args, random_m):
            func(arg, rand, results)            

        print_matrix(results)

if __name__ == '__main__':
    res = []
    unroll([[0,1,2],[3,4,5],[6,7,8]], sum_proc, 'proc', res)
    #unroll([[0,1,2],[3,4,5],[6,7,8]], sum_thre, 'thre', res)
