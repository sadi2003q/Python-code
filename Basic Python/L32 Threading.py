from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(20):
            print("hello")
            sleep(1)

class Hi(Thread) :
    def run(self):
        for i in range(20):
            print("hi")
            sleep(1)


t1 = Hello()
t2 = Hi()


t1.start()

t2.start()


t1.join()
t2.join()