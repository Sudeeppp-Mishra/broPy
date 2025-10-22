# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represeents the class itself.


# Instance methods = Best for operations on instances of the class (bojects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1
        Student.total_gpa += gpa
        
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count==0:
            return 0
        
        else:
            return f"Average GPA: {cls.total_gpa/cls.count}"
    
    
student1 = Student("Ram", 3.80)
student2 = Student("Krishna", 4.00)
    
print(Student.get_count())
print(Student.get_avg_gpa())
        