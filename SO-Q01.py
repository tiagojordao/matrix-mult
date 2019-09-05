import os

def multiply_matrix(row, col, result):
    process = os.fork()
    if process == 0:
        sum_aux = 0
        for a,b in zip(row, col):
            sum_aux += a * b
            print(a, b, sum_aux)
        result.append(sum_aux)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=(", " if len(matrix[i])-1 != j else ""))
        print(" |")

def unroll(args, func, method, res):
    if method == 'proc':
        for i in args:
            func(i, i, res)
    #print(res)

if __name__ == '__main__':
    res = []
    method = ['proc', 'thre']
    args = [[0,1,2],[3,4,5],[6,7,8]]
    unroll(args, multiply_matrix, method[0], res)
