'''1>> find the  dot product of 2 vector (1,2,-1)(2,0,-1)'''
import numpy as np
arr1=np.array([1,2,-1])
arr2=np.array([2,0,-1])
print(np.dot(arr1,arr2))

'''2>> use vectorization feature to add two arrange of size 3*4'''
arr=np.arange(1,13).reshape(3,4)
arr1=np.arange(1,13).reshape(3,4)
arr2=arr+arr1
print(arr2)


'''3>> use vectorization  to divide a 3d array by 5'''
arr=np.arange(1,25).reshape(2,3,4)
print(arr/5)

'''4>> wap to input an array and find min element'''
arr=np.empty((3,4))
print(arr.min())


'''5(a)>> cross product'''
arr1=np.array([3,-4,2])
arr2=np.array([1,-2,0])
print(np.cross(arr1,arr2))


'''5(b)>> cross product'''
arr1=np.array([2,-3,-3])
arr2=np.array([4,-2,1])
print(np.cross(arr1,arr2))
