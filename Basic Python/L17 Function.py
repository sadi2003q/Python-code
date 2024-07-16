def addition(x, y): # pass by value
    return x + y
def doubleValue(x, y):
    return(x, y)

def printname():
    print("i am sadi")

def summation(a, *b): # don't know what would be the value (touple or single variable)
    for i in b:
        a += i
    return a

def unnecessaryParameter(name, age=10):
    print(name)
    print(age)
def passSomething( name , age):
    print(name)
    print(age)


passSomething(age= 21, name="sadi")



