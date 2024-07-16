a = 5
b = 6
print(a+b)
# magic functions
print(int.__add__(a,b))
print(int.__sub__(a, b))
print(int.__mul__(a, b))
print(int.__divmod__(a, b))


class student :
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other): # operator overloading
        return student(self.num1 + other.num1, self.num2 + other.num2)
    def __gt__(self, other): # operator overloading
        s1 = self.num2 + self.num1
        s2 = other.num1 + other.num2

        return s1 > s2

s1 = student(56, 42)
s2 = student(48, 55)

s3 = s1 + s2

print(s3.num1)

print (s1 < s2)