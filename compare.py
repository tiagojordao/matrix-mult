import os
import random
import threading

sem = threading.Lock()
sem2 = threading.Lock()

def random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append([])
            matrix[i][j] = random.randint(0,10)
    return matrix

def sum_matrix(matrix_a, matrix_b):
    matrix = []
    for a, b in zip(matrix_a, matrix_b):
        aux = []
        for i in range(len(a)):
            aux.append(b[i]+a[i])
        matrix.append(aux)
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()

def func(*args):
    for arg in args:
        print(str(arg), end=", ")
    print()

def func_thread(args, random_m, results):
    global sem
    global sem2

    threading.currentThread()

    # regiao crítica
    sem2.acquire()
    sem.acquire()        

    print("\n---- Args ----")
    for i in args:
        results.append(func(*i))
    
    print("\n---- Aleatoria ----")
    for i in random_m:
        results.append(func(*i))

    sem.release() # finalizando função

def unroll(args, func, method, results):
    random_m = random_matrix(len(args), len(args[0]))

    if method == 'thre':
        t1 = threading.Thread(target=func_thread, args=(args,random_m, results))
        t1.start()

        sem2.release()
        sem.acquire()
        
        matriz = sum_matrix(args, random_m)
        print("\n----- Matriz resultante da soma -----")
        print_matrix(matriz)

        sem.release()
   
    else:
        pid = os.fork() # criar-se um novo processo

        if pid != 0: # val != 0 indica que eh o processo original
            print("---- Args ----")
            for i in args:
                results.append(func(*i)) # *i passa a lista como argumentos para a função func

            print("---- Aleatoria ----")
            for i in random_m:
                results.append(func(*i))

        else: # igual a 0 diz que eh do processo filho
            matriz = sum_matrix(args, random_m)

            print("\n----- Matriz resultante da soma -----")
            for i in matriz:
                func(*i)


if __name__ == '__main__':
    res = []
    #unroll([[0,1,2],[3,4,5],[6,7,8]], func, 'proc', res)
    unroll([[0,1,2],[3,4,5],[6,7,8]], func, 'thre', res)