class Mammal:
    def __init__(self):
        self.name = "Mammal"
    def group(self):
        print("Mammal")
    def walk(self):
        print("Mammal walking!")

class Animal():
    "This is Animal's docstring"
    def __init__(self):
        self.name = "Animal"
    def walk(self):
        print("Animal walking!")
    def eat(self):
        print("I'm eating!")
    def speak(self):
        print("Animal speaking!")

class Dog(Mammal, Animal):
    def __init__(self):
        self.name = "Dog"
    def speak(self):
        print("Bow Wow!")
    def wag(self):
        print("I am wagging my tail!")

class Cat(Animal):
    def __init__(self):
        self.name = "Cat"
    def speak(self):
        print("Meow")
    def purr(self):
        print("Purring!")

class GermanShepherd(Dog):
    def __init__(self, name1 = "GermanShepherd"):
        self.name = name1
    def speak(self):
        print("German - BowWow")

def main():
    a1 = Animal()
    a1.speak()
    d1 = Dog()
    c1 = Cat()
    g1 = GermanShepherd() #instantiating
    g1.walk()
    print(Animal.__doc__)

main()