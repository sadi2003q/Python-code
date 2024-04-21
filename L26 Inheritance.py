class A :
    def method1(self):
        print("This is a method from class A")

class B(A): # single level inheritance
    def method2(self):
        print("This is a method from")

class c(B): # multiplle inheritance inheritance
    def method3(self):
        print("this is a method from C")

class D(A, B): # multi level inheritance
    def method4(self):
        print("this is a method from D")