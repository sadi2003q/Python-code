from array import *
from numpy import *

# Type code   C Type             Minimum size in bytes
#  |      'b'         signed integer     1
#  |      'B'         unsigned integer   1
#  |      'u'         Unicode character  2 (see note)
#  |      'h'         signed integer     2
#  |      'H'         unsigned integer   2
#  |      'i'         signed integer     2
#  |      'I'         unsigned integer   2
#  |      'l'         signed integer     4
#  |      'L'         unsigned integer   4
#  |      'q'         signed integer     8 (see note)
#  |      'Q'         unsigned integer   8 (see note)
#  |      'f'         floating point     4
#  |      'd'         floating point     8
#  |


# val = array('i', [1,2,3,4,5,6,7,8])
# print(val)
# for i in val:
#     print(i)
# help(array)
# new = array(val.typecode, (a for a in val))
#
# print(new)
arr = array('i', [])
x = int(input('enter the value of x'))

for i in range(x):
    arr.append(int(input('value to add ')))

search = int(input('enter the value of search '))

for i in arr:
    if i == search:
        print('found')
        break

# different way of initialising array using numpy
_using_Array = array([1, 2, 3, 4, 5]) #tipical array
_using_linSpace = linspace(0, 16, 14)  
_using_LogSpace = logspace(1, 50, 5)
_using_ARange = arange(1, 15, 2)
_using_zeros = zeros(10)
_using_ones = ones(10)

# functions of array
Array1 = array([1, 2, 3, 4, 5])
Array2 = array([6, 7, 8, 9, 10])

print(Array1 + Array2) # addition of array by index of element
print(Array1 - Array2)
print(min(Array2))
print(max(Array1))
print(sin(Array1))
print(cos(Array2))
print(sqrt(Array1))
print(sum(Array2))

newArray = Array1 # same array with same address


newArray2 = Array1.view() # shallow copy
newArray1 = Array1.copy() # deep copy

