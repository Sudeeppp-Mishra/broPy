from car import Car

car1 = Car("Mustang", 2025, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()