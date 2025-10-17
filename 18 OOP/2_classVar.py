# Class variables = Shared among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year = 2025
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students+=1 # we won't use self rather use class cuz we are incrementing the class variable not only for one instance (object)
        
        
student1 = Student("Ram", 18)
student2 = Student("Krishna", 19)

print(student1.name)
print(student1.age)

print(student1.class_year)

print(student2.name)
print(student2.age)

print(student2.class_year)

# Even tho we can access class varible by any object it's good practice to access class variable by class name
print()
print(Student.class_year) # helps with clarity and readability

print("\n", Student.num_students)

print()

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)