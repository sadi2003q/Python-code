class A:
    def show(self):
        print('Show from class A')

class B(A):
    pass
b = B()
print(b.show())

class C(A):
    def show(self):
        print('Show from class C')
c = C()
print(c.show())