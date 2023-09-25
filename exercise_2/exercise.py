import numpy as np

print("enter the elemnts of array1")
array1 = map(int, input().split())
array1 = np.array(list(array1))
print("enter the number of rows and column")
row,column = map(int, input().split())
array1 = array1.reshape(row,column)
print(array1)


print("enter the elemnts of array2")
array2 = map(int, input().split())
array2 = np.array(list(array2))
print("enter the number of rows and column")
row,column = map(int, input().split())
array2 = array2.reshape(row,column)
print(array2)


#dot product

print("Dot product \n")
print(np.dot(array1,array2))

#transpose

print("Transpose of matrix 1 \n")
print(np.transpose(array1))
print("Transpose of matrix 2 \n")
print(np.transpose(array2))

#trace

print("Trace of matrix 1 = "+str(np.trace(array1)))
print("Trace of matrix 2 = "+str(np.trace(array2)))

#rank 

print("Rank of matrix 1 = "+str(np.linalg.matrix_rank(array1)))
print("Rank of matrix 2 = "+str(np.linalg.matrix_rank(array2)))

#determinant

print("Determinant of matrix 1 = "+str(np.linalg.det(array1)))
print("Determinant of matrix 2 = "+str(np.linalg.det(array2)))


#inverse

print("Inverse of matrix 1 \n")
print(np.linalg.inv(array1))
print("\n Inverse of matrix 2 \n")
print(np.linalg.inv(array2))

#eigen value and eigen vector

print("matrix 1 \n")
print(np.linalg.eig(array1))
print("\n matrix 2")
print(np.linalg.eig(array2))
