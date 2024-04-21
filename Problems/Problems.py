# Generating Fibonacci Sequence
from numpy import *
limit = int(input("Enter the value of limit : "))
sequence = []

for i in range(limit):
    if i == 0:
        sequence.append(0)
    elif i==1:
        sequence.append(1)
    else :
        sequence.append(sequence[i-1]+sequence[i-2])
print("Sequence of Fibonacci numbers : ",sequence)


# generating Fibonacci number using recursion
def fibonacci(n, number=0):
    if number == n:
        return
    if number==0:
        sequence.append(0)
    elif number==1:
        sequence.append(1)
    else :
        sequence.append(sequence[number-1]+sequence[number-2])
    fibonacci(n, number+1)

fibonacci(limit)

print("Sequence of Fibonacci numbers : ",sequence)

