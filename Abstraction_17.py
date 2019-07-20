# Four pillars of Object Oriented Programing
# Abstraction
#Given the user only the information needed to perform a task.
#While keeping unnecessary information away.
# Using python modules as an example of abstraction.



class Animal():
# if you put attributes here it will belong to the class

    def __init__(self,age, weight, species): # attributes and qualities # declaring a variable that belongs to an object when you create one
        self.age =age # same as age=15 in non oop
        self.weight =weight
        self.species = species

    def can_hunt(self, value):
         return value

    def eat(self):
        return 'Yummmy'

    def sleep(self):
        return "zzzzzzzzzz"


 # Use this super init to call the method/ attributes from Animal to intialize me
class mammals(Animal):
    def __init__(self,age,weight,species,name):
        super().__init__(age,weight,species)
        self.name = name

    def can_speak_language(self,value):
        return value

class Birds(Animal):
    def __init__(self,age,weight,species,name,feather_color):
        super().__init__(age,weight,species)
        self.name = name
        self.feather_color = feather_color

    def can_fly(self, can_fly):
        return can_fly

class Reptiles(Animal):
    def __init__(self, age, weight, species, name, region_found):
        super().__init__(age,weight,species)
        self.region_found = region_found

    def is_venomous(self,value):
        return value


