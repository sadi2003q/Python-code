class student:
    school = 'Mathematics'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # basic function related to print all attributes
    def show_info(self):
        print(self.name, self.age)

    # functions to print global variable for all object
    @classmethod
    def show_info2(cls):
        print(cls.school)

    # function to do something not related to attributes
    @staticmethod
    def show_info3():
        print('nothing is important')



sadi = student('sadi', 21)
sadi.show_info()
sadi.show_info2()
sadi.show_info3()