# "Duck Typing " = Another way to achieve polymorphism besides Inheritance
#                  Object must have the min. necessary attributes/methods
#                  "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    
    alive = False
    
    
    def speak(self):
        print("Honk!")
        
animals = [Dog(), Cat(), Car()] # although Car() doesn't belong to animal as long as it has minimu attributes/methods it can be used here

for animal in animals:
    animal.speak()
    print(animal.alive)
    