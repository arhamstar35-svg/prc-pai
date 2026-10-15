import numpy as np

arr = np.arange(1, 13)
matrix = arr.reshape(4,-1 )
print(matrix)
print(matrix.shape)

arr = np.array([[1, 2], [3, 4]])
print(arr.flatten())
print(arr.ravel())
arr=np.arange(12)
ina=arr.reshape(2,2,3)

arr2=np.array([10,30,11,22,77])

print(arr2>25)
print(arr2[arr2>25])


print(np.where(arr2>20))

rng=np.random.default_rng(42)

matrix=rng.integers(0,100,size=(2,3))
print(matrix)