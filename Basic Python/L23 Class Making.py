class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)

sadi = student('Sadi', 12)
sadi.printInfo()