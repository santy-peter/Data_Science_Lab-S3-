import numpy as np
n1=np.arange(16).reshape(4,4)
print(n1)
np.savetxt('7_array.txt', n1, fmt="%d")
print(np.loadtxt('7_array.txt'))

