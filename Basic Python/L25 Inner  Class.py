class computer:
    def __init__(self, name, ram , processor, gpu):
        self.name = name
        self.lap = self.laptop(ram,processor, gpu)
    def showInformation(self):
        print("Name : ", self.name)
        self.lap.showInformation()

    class laptop:
        def __init__(self, ram, processor, gpu):
            self.ram = ram
            self.processor = processor
            self.gpu = gpu

        def showInformation(self):
            print("RAM : ", self.ram)
            print("Processor : ", self.processor)
            print("GPU : ", self.gpu)

comp = computer("HP", 16, "i5", 1660)
comp.showInformation()