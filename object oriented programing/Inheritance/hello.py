class Animal:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def full_name(self):
        return f'{self.name} {self.place}'


class Dog(Animal):
    pass

dog=Dog("jhonny",10,"africa")

print(dog.name)
print(dog.age)
print(dog.place)
print(dog.full_name())

#inheritace is parent class propetice and methord transfer child class