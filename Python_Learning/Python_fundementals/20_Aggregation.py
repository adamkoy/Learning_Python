# When a class has another class as a property or attribute
# We have an aggregate or association relationship
# If the contained member outlives the main class then we have an aggregation
# If on the other hand the contained member has the same life time as the
#main class then we have an association.

#Car stereo can be modelled as an object.

class Car ():
    def __init__(self, model, make):
        self.model = model
        self.make = make


class Engine():
    def  __init__(self,size ,fuel_type, horse_power):
        self.size = size
        self.fuel_type = fuel_type
        self.horse_power = horse_power


    def rev(self):
        print("jrum")

v8=Car.(8,"petrol",1000)
