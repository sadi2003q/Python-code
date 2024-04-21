from numpy import *


# Finding Even and Odd number together
def count(list):
    evenNumber = 0
    oddNumber = 0

    for number in list:
        if number % 2 == 0:
            evenNumber += 1
        else:
            oddNumber += 1

    return evenNumber, oddNumber


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNumber, oddNumber = count(list)

print("Even Number {} Odd Number {}".format(evenNumber, oddNumber))


# Finding n Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return
    if n <= 1:
        print(n)

    a = 0
    b = 1
    for num in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
fibonacci(12)

# Findig Factorial using recursion

def factorial(n) :
    if n==1 :
        return 1
    else:
        return n*factorial(n-1)

print(factorial(9))