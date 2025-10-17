# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

# class Circle:
#     def __init__(self, color, is_filled, radius):
#         self.color = color
#         self.filled = is_filled
#         self.radius = radius

# class Square:
#     def __init__(self, color, is_filled, width):
#         self.color = color
#         self.filled = is_filled
#         self.width = width


# class Triangle:
#     def __init__(self, color, is_filled, width, height):
#         self.color = color
#         self.filled = is_filled
#         self.width = width
#         self.height = height

# as we can see there are comman variables and we don't want to reuse them instead we can do:


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self): # Method overriding
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
        
    def describe(self): # Method overriding
        super().describe()
        print(f"It is a square with an area of {self.width ** 2}")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
    def describe(self): # Method overriding
        super().describe()
        print(f"It is a triangle with an area of {1/2 * self.width * self.height}")


circle = Circle(color="red", is_filled=True, radius=4)
square = Square(color="blue", is_filled=False, width=8)
triangle = Triangle(color="cyan", is_filled=True, height=10, width=3)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()

print()

print(square.color)
print(square.is_filled)
print(square.width)
square.describe()

print()

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()