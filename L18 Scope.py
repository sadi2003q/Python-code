
a = 21
print('print something')
def printSomething() :
    print("inside function ", a) #21
    return
printSomething()
print("outside the function ",a) #21


print('print Scope')
def printScope():
    a = 12
    print("inside function ", a) #12
printScope()
print("outside function ", a) #21

print('print Scope2')
def printScope2() :
    global a
    a = 5
    print("inside function ", a) # 5
printScope2()
print("outside function ", a) # 5


print('print Scope3')
def printScope3() :
    x = globals()['a']
    print("inside function ", x) # 21
    x = globals()['a'] = 7
    print("inside function ", x) # 7
printScope3()
print("outside function ", a)# 7