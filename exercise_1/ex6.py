import numpy as np
arr=np.array([[1,2],[2,3]])
print(arr)

print(np.sum(arr))

print(np.sum(arr, axis=0)) //column sum

print(np.sum(arr, axis=1)) //row sum
