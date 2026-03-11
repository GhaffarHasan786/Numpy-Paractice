#ndim is used for to find out the number of dimentional in array

import numpy as np
array_1d = np.array([1,2,3,4])
array_2d = np.array([[1,2,3],[2,3,4]])
array_3d = np.array([[[1,2,3,4],[1,5,7,8]]])

print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)
