from numpy import *

array = array([[1,2,3],
               [4,5,6],
                [4,5,6] ])

print(array.ndim)
print(array.shape)
print(array.size)


flatArray = array.flatten()
reShapeArray = flatArray.reshape(2, 3)

m1 = matrix(array) #initialising matrix from array
m2 = matrix('1 2 3;4 5 6;7 8 9')   #initialising matrix from number

print(m1)
print(m2)
print(diagonal(m1))
print(m1.max())

m3 = m1*m2
print(m3)