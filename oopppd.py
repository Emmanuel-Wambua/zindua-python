class Person:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def eat(self,car):
        return f"{self.name} is {self.age} years old and wants to buy a {car}"
    

class Child(Person):
    def __init__(self, name, age, nationality,generation,education):
        super().__init__(name, age, nationality)
        self.generation = generation
        self.education = education
myChild = Child("James",74,"American","Gen X","University")

rut = myChild.eat("Dodge challenger")

print(rut)