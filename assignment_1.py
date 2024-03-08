import numpy as np
#(1) Create 2D array of 3X4 from numbers 12 to 24 and fetch 16,19,14
arr=np.arange(12,24).reshape(3,4)
print("16: ",arr[1][0])
print("19: ",arr[1][3])
print("14: ",arr[0][2])

#(2) Create 3D array of 2X3X4 of first 24 whole numbers and fetch 16,4,0
arr=np.arange(0,24).reshape(2,3,4)
print(arr[1,1,0])
print(arr[0,1,0])
print(arr[0,0,0])

#(3)
arr=np.arange(5,51,5)
print(arr[arr%4==0])

#(4)
arr=np.arange(1,21)
print(arr[np.logical_and(arr>5,arr<12)])

#(5)
arr=np.arange(5,51,5)
print(arr[(arr%3==0)|(arr%4==0)])

#(6)
arr=np.arange(1,25).reshape(2,3,4)
for i in np.nditer(arr):
    print(i)

#(7)
arr=np.arange(1,25).reshape(2,4,3)
for pos,i in np.ndenumerate(arr):
    print(pos,i)
