class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    
    def say_my_name(self):
        return f"Здраствуйте, меня зовут {self.name}"

class Student(Person):
    def __init__(self, grades):
        self.__grades = grades

    def __str__(self):
        return self.__grades

    def show_grades(self):
        return self.__grades

# class Teacher(Person):
#     def __str__(self):
#         return f"профессор {say_my_name}

person = Person('ASa', 120)

student = Student (100)
student.show_grades()

# teacher = Teacher()

print(person.say_my_name())
print(student.show_grades())
# print(teacher)
# print(student.show_grades())