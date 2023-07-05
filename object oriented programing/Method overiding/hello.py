class Animal:
    def __init__(self,place):
        self.place=place
    def full_name(self):
        return f'{self.place}'


class Dog(Animal):
    def __init__(self,name):
        super().__init__("Dog")
        self.name=name

    def full_name(self):
        return "hello"

animal= Animal("cat")

dog=Dog("jhonny")

print(dog.place)


