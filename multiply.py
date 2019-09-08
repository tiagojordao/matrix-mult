import os
import random
import threading

def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0,10)
    return matrix

def process_multiply(row_a, row_b, results):
    pid = os.fork()
    if pid == 0:
        aux = []
        for a, b in zip(row_a, row_b):
            aux.append(a + b)

        results.append(aux)  

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
    random_m = random_matrix(len(args), len(args[0]))

    if method == "thre":
        threads = []
        cols = len(random_m[0])
        rows = len(random_m)

        results = [[0 for i in range(cols)] for j in range(len(args))]

        for j in range(cols):
            aux = []
            for i in range(rows):
                aux.append(random_m[i][j])
            for idx, arg in enumerate(args):
                threads.append([])
                threads[-1] = threading.Thread(target=func, args=(idx, j, arg, aux, results))
                threads[-1].start() 

        print_matrix(results)
    
    else: 
        processos = []

        for arg, row_aleatoria in zip(args, random_m):
            processos.append([])
            func(arg, row_aleatoria, results)            

        print_matrix(results)

if __name__ == '__main__':
    res = []
    unroll([[0,1,2],[3,4,5],[6,7,8]], process_multiply, 'proc', res)
    #unroll([[0,1,2],[3,4,5],[6,7,8]], thre_multiply, 'thre', res)
