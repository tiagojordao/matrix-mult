import matplotlib.pyplot as plt
fig, ax = plt.subplots( nrows=1, ncols=1 ) 
ax.plot([0,1,2], [10,20,3])
ax.plot([0,1,2], [10,25,3])
fig.savefig('compare.png') 
plt.close(fig)