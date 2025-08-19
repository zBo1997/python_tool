class Dog:
    age= 0
    name = ""
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def printClassInfo(self):
        print(self)
        print(self.__class__)

dog = Dog(1, "dog1")

print(dog.age)
dog.printClassInfo()
