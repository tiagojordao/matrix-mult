# -*- coding: utf-8 -*-
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

#funçao que recebe as duas matrizes e realiza a soma
def sum_matrix(matrix_a, matrix_b):
    start_time = datetime.datetime.today()
    matrix = []
    for a, b in zip(matrix_a, matrix_b):
        aux = []
        for i in range(len(a)):
            aux.append(b[i]+a[i])
        matrix.append(aux)
    end_time = datetime.datetime.today()
    time_in_program = end_time - start_time
    with open('sequencial_sum_result.txt', 'a') as file:
        file.write(str(time_in_program.total_seconds())+"\n")
    return matrix

#funçao que recebe as duas matrizes e realiza a multiplicacao
def multiply_matrix(matrix_a, matrix_b):
    rows_A = len(matrix_a)
    cols_A = len(matrix_a[0])
    rows_B = len(matrix_b)
    cols_B = len(matrix_b[0])
    start_time = datetime.datetime.today()
    matrix = []
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += matrix_a[i][k] * matrix_b[k][j]
    end_time = datetime.datetime.today()
    time_in_program = end_time - start_time
    
    with open('sequencial_multiply_result.txt', 'a') as file:
        file.write(str(time_in_program.total_seconds())+"\n")
    return C
    
#print das matrizes
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="   ")
        print()


def unroll(args, results):
    matrix_a = args[0]
    matrix_b = args[1]
    matrix_result_sum = sum_matrix(matrix_a,matrix_b)
    matrix_result_mult = multiply_matrix(matrix_a,matrix_b)
    # print_matrix(matrix_result_sum)
    # print_matrix(matrix_result_mult)

if __name__ == '__main__':
    res = []
    args = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
    vals = [1,2,3,4,5,6,8,10,20,30,40,50,75,100]
    for i in vals:
        r1 = random_matrix(i,i)
        r2 = random_matrix(i,i)
        args2 = [r1,r2]
        unroll(args2, res)
   
    # unroll(args, func, 'thre', res)