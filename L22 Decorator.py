def division(a, b) :
    return a/b

def smart_division(func):
    def inner(a, b):
        if a<b :
            a, b = b, a
        return func(a, b)
    return inner
division = smart_division(division)

print(division(2, 4))

def multiplication(a, b) : return a * b

def smart_Multiplication(func):
    def inner(a, b):
        if a>b :
            a = 1
        return func(a, b)
    return inner
multiple = smart_Multiplication(multiplication)

print(multiple(10, 20))