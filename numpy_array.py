import numpy as np
import time

size=10000000
list1=list(range(size))
list2=list(range(size))

start_time=time.time()
result=[x+y for x,y in zip(list1,list2)]
end_time=time.time()
print("the time taken by the python list:",end_time-start_time)

# numpy array
arr2=np.array(list2)
arr1=np.array(list1)


start_time=time.time()
result=arr1+arr2
end_time=time.time()
print("the time taken by the numpy array:",end_time-start_time)

# numpy size

import numpy as np

# Creating a 1D NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D NumPy array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Checking type and shape
print("Type:", type(arr1))
print("Shape:", arr2.shape)