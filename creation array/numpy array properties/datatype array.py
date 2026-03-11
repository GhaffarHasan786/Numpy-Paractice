# this function is used for find the the datatype 


import numpy as np
array_data = np.array([10,30,40.3,50])
print(array_data.dtype)

#change data type of array by using astype() function

import numpy as np
array = np.array([1.2,2.3,2.1])
print(array.dtype)
int_array = array.astype(int)
print(int_array)
print(int_array.dtype)

