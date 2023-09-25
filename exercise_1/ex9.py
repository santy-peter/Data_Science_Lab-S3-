import numpy as np

numz = np.arange(16).reshape(4,4)
print("Original array:")
print(numz)

print("\n after swapping:")

//numz = numz[[-1,1,2,0]]
numz[[0,-1],:]=numz[[-1,0],:]
print(numz)
