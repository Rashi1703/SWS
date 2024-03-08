import numpy as np
#(1)#D array---flatten it
arr=np.arange(1,25).reshape(2,3,4)
arr1=np.ndarray.flatten(arr)
print(arr1)

#(2)diff between flatten and ravel
#~~~~~flatten-copy(method)~~~~~~~~ravel-view(function)
arr=np.arange(1,13).reshape(4,3)
arr1=np.ndarray.flatten(arr)
print(arr1)
arr1[0]=100
print(arr1)
print(arr)

arr=np.arange(1,13).reshape(4,3)
arr1=np.ravel(arr)
print(arr1)
arr1[0]=100
print(arr)
print(arr1)

#(3)2D array----transpose
arr=np.arange(1,13).reshape(4,3)
arr1=np.transpose(arr)
print(arr)
print(arr1)

#(4)3D array---transpose it on axes (2,0,1)
arr=np.arange(1,25).reshape(2,3,4)#axes:(2,3,4)~~~(0,1,2)
arr1=np.transpose(arr,axes=(2,0,1))#4X2X3
print(arr)
print(arr1)

#(5)4D array----swap 2 and 4 axes
arr=np.arange(1,49).reshape(2,2,4,3)
arr1=np.swapaxes(arr,1,3)
print(arr)
print(arr1)

#(6)Concatenate in array
a=np.array([10,20,30])
b=np.array([40,50,60])
c=np.concatenate((a,b))
print(c)

a=np.arange(1,13).reshape(3,4)
b=np.arange(13,25).reshape(3,4)
print(a)
print(b)
#axis=0
c=np.concatenate((a,b),axis=0)
print(c)
#axis=1
d=np.concatenate((a,b),axis=1)
print(d)
#axis=None
e=np.concatenate((a,b),axis=None)
print(e)


#(7)stack on array
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[10,20,30],[40,50,60]])
c=np.stack((a,b),axis=0)
print(c)
d=np.stack((a,b),axis=1)
print(d)

