import numpy as np
'''(1)Slicing'''
arr=np.arange(1,25).reshape(2,3,4)
#17
print(arr[1,1,0])
#3
print(arr[0,0,2])
#19
print(arr[1,1,2])
#24
print(arr[1,2,3])
'''(2)'''
#5,6,7
print(arr[0,1,:3])
#9 10
#21 22
print(arr[:,2,:2])
'''(3)Table of 5 fetch values divisible by 4 using advance indexing'''
arr=np.arange(5,51,5)
l=[3,7]
print(arr[l])
'''(4)'''
arr=np.arange(1,13).reshape(3,4)
#12,7,3,9 using advance indexing
print(arr[[2,1,0,2],[3,2,2,0]])
