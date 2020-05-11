class Animal:
    def __init__(self, name,):
        self.name = name
    def makeNoise(self):
        pass
class Dog(Animal):
    def makeNoise(self):
        print(self.name + " says: Woof!")
    def eat(self):
        print(self.name + " eats: Meat")
class Cat(Animal):
    def makeNoise(self):
        print(self.name + " says: Meow!")
    def eat(self):
        print(self.name + " eats: KitKat!")
dog = Dog("Baxter")
cat = Cat("Julie")
dog.makeNoise()
dog.eat()
cat.makeNoise()
cat.eat()

