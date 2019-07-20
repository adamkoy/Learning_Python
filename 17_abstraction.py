from Abstraction_17 import Reptiles

class Snake(Reptiles):
    def __init__(self, age, weight, species,name,region_found, num_fangs,length):
        super().__init__(age,weight,species,name, region_found)
        self.num_fangs = num_fangs
        self.length = length

    def can_constrict(self, bool_value):
        return bool_value

    def can_swim(self, boo1_value):
        return boo1_value


python =Snake(35,450,"pyhtoras terroriza","Bop","moorgate",0,12)
print(python.length)
print(python.species)
print(python.region_found)
print(python.num_fangs)
print(python.age)
print(python.weight)

print(python.can_constrict(True ))