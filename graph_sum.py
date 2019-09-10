import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() 
labels = (1,2,3,4,5,6,8,10,20,30,40,50,75,100)
vals = []
vals2 = []
vals3 = []

vals4 = []
vals5 = []
vals6 = []

with open("sequencial_sum_result.txt", "r+") as f:
    for line in f.readlines():
        vals.append(float(line))
with open("result_thread_sum.txt", "r+") as f:
    for line in f.readlines():
        vals2.append(float(line))
with open("result_proc_sum.txt", "r+") as f:
    for line in f.readlines():
        vals3.append(float(line))
        
# Make a fake dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(vals))
 
# Create bars
plt.plot(y_pos, vals, label="Soma sequêncial")
plt.plot(y_pos, vals2, label="Soma thread")
plt.plot(y_pos, vals3, label="Soma processos")
plt.legend()
 
# Create names on the x-axis
plt.xticks(y_pos, labels)
 
# Show graphic
plt.savefig('result_sum_seq.png')
plt.close(fig)
