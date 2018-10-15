import csv
import numpy as np

#The with statement is useful as it closes the file for us after and we no longer
#need the line file.close(). The second optional argument of the open() function is
#mode and 'r' is for reading.

#with open('winequality-red.csv', 'r') as file:
#    wines = list(csv.reader(file, delimiter = ';'))
#print(wines[:3])

#python slice notation, [start:end] all items from start to end - 1. Also
#if we count from the back [-1] represents last element wine is now a list of lists
#with each list representing a row, so this prints first three rows

#We want to find the average of the qualities, ie sum all the last column elements and divide by length

#qualities = [float(item[-1]) for item in wines[1:]]
#print(sum(qualities) / len(qualities))

#A better method will be to use numpy arrays:

wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)

wines = np.array(wines[1:], dtype = np.float)
print(wines)
#This gives a 2D array excluding the header column (I guess now this starts indexing at 0?),
#since for a numpy array all entries have to be of the same type.
print(wines.shape)
