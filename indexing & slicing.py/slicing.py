""""
array[start:stop:step]
array[start:stop] start to end -1
array[::step]
array[::-1] negative step revese the array
"""

import numpy as np
arr = np.array([10,56,89,90,6,9])
print(arr[1:5:2])
print(arr[1:5])
print(arr[::2])
print(arr[::-1])
print(arr[1::2])
