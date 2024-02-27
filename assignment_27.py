import numpy as np
'''(1)Create a 2D array of 3X5 using numbers with array function'''
arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr)
'''(2)first 20 whole numbers using arange function'''
arr=np.arange(20)
print(arr)
'''(3)linspace function---12 linearly spaced values between 10 and 50, all values-integer'''
arr=np.linspace(10,50,12,dtype=int)
print(arr)
'''(4)4 dimensional array,each must contain 2 three dimensional array,each 3-D array contain 4 2-D of 3X4,they all must be filled the number 5'''
arr=np.full((2,4,3,4),5)
print(arr)
'''(5)identity matrix 5X5---complex data type'''
arr=np.identity(5,dtype='complex')
print(arr)
'''(6)eye function---5X5---k=2---datatype=int'''
arr=np.eye(5,5,k=2,dtype=int)
print(arr)
'''(7)write code to extract k=-1 diagonal from 2D matrix'''
arr=np.array([[1,0],[0,1]])
arr=np.diag(arr,k=-1)
print(arr)
'''(8)Create an array 3X4 using emplty function'''
arr=np.empty((3,4))
print(arr)
'''(9)create an 2D array 3X4 using random numbers from 10 to 20(20 is inclusive)'''
arr=np.random.randint(10,21,(3,4))
print(arr)
'''(10)create a 3D array of random number from 0 to 100, size is 5X6 and these must be 4 2D array'''
arr=np.random.randint(0,100,(4,5,6))
print(arr)

