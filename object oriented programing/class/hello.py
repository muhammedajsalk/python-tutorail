class Student:
    first_name="ajsal"
    last_name="N"
    student_class=1
    divition="c"

    def full_name(self):
        return  f"{self.first_name} {self.last_name}"


student1=Student()
student2=Student()

print(student1.full_name())
print(student2.full_name())