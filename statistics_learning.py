import numpy as np
from statistics import mode

data = np.array([10, 20, 20, 30, 40])
"""print(np.mean(data))"""

# median = middle value after sort data
# print(np.median(data))

# Mode — most frequent
# print(mode(data))

# range diff btwn max and min val
print(np.max(data) - np.min(data))

# important ML concept.
""" => 48, 49, 50, 51, 52
mean = 50
48 → 2 away
49 → 1 away
50 → 0 away
51 → 1 away
52 → 2 away
numbers are close to the mean.
conclusion : The data is not very spread out.

=> 10, 30, 50, 70, 90
mean = 50
10 → 40 away
30 → 20 away
50 → 0 away
70 → 20 away
90 → 40 away
The numbers are farther from the mean.
conclusion : The data more spread out.

"""
import matplotlib.pyplot as plt

"""data = np.array([48, 49, 50, 51, 52])

plt.scatter(data, np.zeros(len(data)))
plt.axvline(np.mean(data), linestyle="--")

plt.show()"""

"""data = np.array([10, 30, 50, 70, 90])

plt.scatter(data, np.zeros(len(data)))
plt.axvline(np.mean(data), linestyle="--")

plt.show()"""

data = np.array([10, 30, 50, 70, 90])

plt.hist(data)
plt.show()