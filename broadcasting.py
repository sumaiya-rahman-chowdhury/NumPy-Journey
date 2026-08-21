import numpy as np

"""
performs operations on different shape of array . automatically strecthes array

result = arr + 10
arr:       [1  2  3]
10:        [10 10 10]   ← NumPy conceptually stretches 10

result:    [11 12 13]

"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

# print(arr1 + arr2)


# Broadcasting a 1D array across a 2D array
# arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# arr2 = np.array([10, 20, 30])

# print(arr1 + arr2)

""" how its works : 
    [1 2 3
    4 5 6] + [10 20 30
              10 20 30]
    = [
    1+10 2+20 3+30
    4+10 5+20 6+30
    ]
   ans =  [11 22 33
           14 25 36]
"""
# done

# Very important example: (3, 1) + (1, 4)
"""
arr1 = np.array([
    [1],
    [2],
    [3]
])

arr2 = np.array([[10, 20, 30, 40]])

print(arr1.shape)
print(arr2.shape)

"""
""" how its works :
[
    [1 1 1 1 ],
    [2 2 2 2 ],
    [3 3 3 3 ]
] + [[10, 20, 30, 40
     10, 20, 30, 40
     10, 20, 30, 40
]]
=[[
11 21 31 41
12 22 32 42
13 23 33 43
]]
"""
#Final Broadcasting Challenge! 🔥
"""
(5, 3)
(3,) =>
5 vs 1 
3 vs 3
so broadcasting works
(2, 3, 4)
(3, 1) =>
(2, 3, 4)
(1, 3, 1)
2 vs 1 
3 vs 3
4 vs 1
working
(3, 2)
(2, 1)
not works
(2, 1, 3, 4)
(1, 5, 1, 4)
2 vs 1
1 vs 5
3 vs 1
4 vs 4
 working
 
"""
