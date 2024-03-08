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

#(10)
arr=np.arange(1,12)
arr1=np.resize(arr,(5,6))
print(arr1)

#(11)
arr=np.arange(7,71,7)
arr.resize((4,5))
print(arr)
