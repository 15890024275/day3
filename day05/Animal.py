class Animal():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃东西")

    def __str__(self):
        return self.name

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def bark(self):
        print("叫")
    def __str__(self):
        return self.name

d = Dog("D",3)
print(d)
d.bark()
d.eat()
