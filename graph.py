import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() 
labels = (1,2,3,4,5,6,8,10,20,30,40,50,75,100)
vals = []
with open("sequencial_sum_result.txt", "r+") as f:
    for line in f.readlines():
        print(line)
        vals.append(line)
# Make a fake dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(vals))
 
# Create bars
plt.bar(y_pos, vals)
 
# Create names on the x-axis
plt.xticks(y_pos, labels)
 
# Show graphic
plt.show()
plt.savefig('books_read.png')
plt.close(fig)
