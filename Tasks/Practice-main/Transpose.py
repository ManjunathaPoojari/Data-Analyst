# if the original matrix and transpose matrix are same ==print same else not same.

import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.zeros([2,2])
for i in range(2):
    for j in range(2):
        arr2[j,i]=arr1[i,j]
if np.array_equal(arr1,arr2):
    print("same because all elements are identical")
else:
    print("not same")