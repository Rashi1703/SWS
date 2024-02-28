'''(1)array of random integer from 30 to 40---2D array (3X4)'''
import numpy as np
arr=np.random.randint(30,40,(3,4))
print(arr)

'''(2)to get a random numberr from 1 to 6 and their probability must be uniformly distributed---2D array (2X4)'''
arr=np.random.uniform(1,6,(2,4))
print(arr)

'''(3)random number close to 5 with variance 2 to get 50 numbers'''
arr=np.random.normal(5,2,50)
print(arr)

'''(4)3D array for random number between 0 to 1'''
arr=np.random.rand(3,2,4)
print(arr)

'''(5)table of 10 using arange function and shuffle it'''
arr=np.arange(10,101,10)
print(arr)
np.random.shuffle(arr)
print(arr)

'''(6)2D array and find its properties'''
arr=np.array([[10,20,30],[30,40,50],[50,60,70],[10,40,20]])
print("Arr: ",arr)
print("ndim: ",arr.ndim)
print("shape: ",arr.shape)
print("size: ",arr.size)
print("dtype: ",arr.dtype)
print("itemsize: ",arr.itemsize)

'''(7)difference btw view and copy'''
#shallow copy---view
arr=np.array([10,20,30,40,50])
arr1=arr.view()
arr1[0]=100
print(arr)
print(arr1)
#deep copy---copy
arr=np.array([10,20,30,40,50])
arr1=arr.copy()
arr1[0]=100
print(arr)
print(arr1)

'''(8)Make 2D array and fetch 50'''
arr=np.array([[10,20,30,40],[7,8,9,10],[10,50,60,6]])
print(arr[2][1])
