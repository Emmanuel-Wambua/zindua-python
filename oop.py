# class - a blueprint for creating an object
# object - instance of a class

class Person:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    

myPerson = Person("James",74,"American")

rut = myPerson.name

print(rut)