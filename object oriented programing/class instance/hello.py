class Student:
    def __init__(self,first_name,last_name,student_class,divition):
        self.first_name=first_name
        self.last_name=last_name
        self.student_class=student_class
        self.divition=divition

    def full_name(self):
        return  f"{self.first_name} {self.last_name}"


student1=Student("ajsal","k",4,"D")
student2=Student("jaseel","k",6,"c")

print(student1.full_name())
print(student2.full_name())