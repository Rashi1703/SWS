import numpy as np
#(1)
a=np.array([[10],[20],[30]])
b=np.array([1,2,3])
print(a+b)

'''output-
[[11 12 13]
 [21 22 23]
 [31 32 33]]
'''

#(2)
a=np.array([[10,20],[30,40],[50,60]])
b=np.array([5])
print(a%b)

'''output-
[[0 0]
 [0 0]
 [0 0]]
'''

#(3)
a=np.array([[10,20,30],[40,50,60]])
b=np.array([5,10])
#print(a*b)~~~~~~~~~Error

#(4)
arr=np.arange(5,51,5).reshape(5,2)
print(arr)

'''
(5)
For the array arr[1......5][1......8], with a base value of 200 and each element size of 4 bytes,
the address of arr[3][7] in row-major order is 288.

(6)
For the array arr[1......6][1......12], with a base value of 500 and each element size of 2 bytes,
the address of arr[5][10] in row-major order is 614.

(7)
For the array arr[1......8][1......10], with a base value of 1000 and each element size of 8 bytes,
the address of arr[6][3] in column-major order is 1168.

(8)
For the array arr[1......4][1......6], with a base value of 300 and each element size of 1 byte,
the address of arr[2][5] in column-major order is 317.

(9)
For the array arr[1......7][1......9], with a base value of 800 and each element size of 16 bytes,
the address of arr[4][8] in row-major order is 1344.
'''

#(10)
arr=np.arange(1,12)
arr1=np.resize(arr,(5,6))
print(arr1)

#(11)
arr=np.arange(7,71,7)
arr.resize((4,5))
print(arr)
