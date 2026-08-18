#0-D array
import numpy as np
arr = np.array(42)
#print(arr)

#1-D array
arr = np.array([1, 2, 3, 4, 5])
#print(arr)

#2-D array
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
#print(a)
#print(a.shape)

#3-D array
a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
#print(a.shape)
#print(a.ndim)

#define number of dimensions arr gonna hv
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.ndim)