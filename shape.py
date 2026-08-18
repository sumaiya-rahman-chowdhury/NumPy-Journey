import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)
#[ [ [ [ [1, 2, 3, 4]]]]]
#print(arr)
#print('shape of array :', arr.shape) 
#output is 1,1,1,1,4

#reshaping array
#change shape , 1D to 2D
newarr = arr.reshape(2, 2, 1, 1, 1)
print(newarr)