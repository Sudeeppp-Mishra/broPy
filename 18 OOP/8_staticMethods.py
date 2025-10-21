# Static Methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod #this decorator is needed to make static method
    def is_valid_position(position): # no need of self here
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Ram", "Manager")
employee2 = Employee("Shyam", "Cook")
employee3 = Employee("Hari", "Cashier")
employee4 = Employee("Krishna", "Janitor")

print(Employee.is_valid_position("Cook"))
print()
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())