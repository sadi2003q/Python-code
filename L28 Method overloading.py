# method overloading using None keyword

def summation(a = None, b = None, c = None):
    if a != None and b != None and c != None :
        return a + b + c
    elif a != None and b != None :
        return a + b
    elif b != None and c != None :
        return b + c
    elif a != None and c != None :
        return a + c
    elif a != None:
        return a;
    elif  b != None :
        return b
    elif c!= None:
        return c

print(summation(2, 3 , 4))
print(summation(1, 10))
print(summation(8))



