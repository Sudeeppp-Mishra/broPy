class Dog:
    def bark(self): 
        print(f"{self} is barking")
        
dog1 = Dog()
dog2 = Dog()

dog1.bark()
dog2.bark()

# here what I wanted u to show is that methods must have the parameter
# self cuz when we do dog1.bark() python reads it like Dog.bark(dog1)
# so self parameter must be there else we will get a TypeError

