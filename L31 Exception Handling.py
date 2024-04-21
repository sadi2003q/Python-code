
a = 5
b = 0

try:
    print(a/b)
except Exception as e:
    print("ZeroDivisionError : ", e)

finally:
    print('out of the function')