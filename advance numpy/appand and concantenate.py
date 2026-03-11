"""
appand fuction use krty ha ik array my value ko jma yani add krny k liye
"""
import numpy as np

arr = np.array([1,2,3,4,5,5])
new_arr = np.append(arr,(7,8))
print(new_arr)

"""
concantenate function is liye use krty ha k ager multiple array ho to un ko add kia jaye yani ik array bnaya jaye
"""
import numpy as np
arr1 = np.array([1,2,3,])
arr2 = np.array([4,5,6])

new_array = np.concatenate((arr1,arr2))
print(new_array)