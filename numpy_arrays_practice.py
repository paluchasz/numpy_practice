import numpy as np

#Create a 3x4 array of zeros
array1 = np.zeros((3,4))
print(array1)
#Create a 6x4 array of ones
array2 = np.ones((6,4))
print(array2)
#concatenate the two arrays in the first axis, so vertically (this works if number of columns is the same)
x = np.concatenate((array1,array2),axis=0)
print(x)
#Get the first column elements
first_column = x[:,0]
print(first_column)
