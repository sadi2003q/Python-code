from abc import abstractmethod, ABC
class A(ABC):

    @abstractmethod
    def method(self):
        pass

class B(A):
    def method(self):
        print("something is not working in this course")


