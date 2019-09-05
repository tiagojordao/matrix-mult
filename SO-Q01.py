import numpy
import os

matrizA = numpy.matrix([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
])
matrizB = numpy.matrix([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
])
for x in matrizA:
    for y in matrizB:
        fork = os.fork()
        if fork == 0:
            print('child process',x,y)
        else:
            print('father process')