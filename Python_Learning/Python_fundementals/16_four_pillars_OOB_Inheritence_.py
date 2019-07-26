# Four pillars of Object Oriented Programing
# Inheritance


class Vehicle():

    def __init__(self,make,color,engine_size,year,speed):
        self.make =make
        self.color =color
        self.engine_size = engine_size
        self.year = year
        self.speed = speed

    def start(self):
        return "vroom"

    def stop(self):
        return "screech"

    def accelerate(self):
        return self.speed++10


class Truck(Vehicle):

    def __init__(self,make,color,engine_size,year, trailer_size,speed):
        super().__init__(make,color,engine_size,year,speed)
        self.trailer_size = trailer_size


class Boat (Vehicle):

    def __init__(self,make,color,engine_size,year,speed):
       super().__init__(make,color,engine_size,year,speed)

    def honk(self):
        return "honk"

    def drop_anker(self):
        return "anker"


my_car = Vehicle("Honda","Red", 1.6,1995, 20)
my_truck= Truck ("Ford","Silver",7.5,2019,14,10)
my_boat = Boat( "Yamaha", "White", 25, 5,80,)

print(my_truck.start())

print(my_truck.accelerate())

print(my_truck.stop())

print("---------------------------------------------------------------------------------------------------------------")

print(f"Omid's truck has a {my_truck.make} of size {my_truck.engine_size} of color {my_truck.color} is {my_truck.year} years old and trailer size {my_truck.trailer_size}")
print(f"Daniel's car has a {my_car.make} of size {my_car.engine_size} of color {my_car.color} is {my_car.year} years old")
print(f"Adam's boat has a {my_boat.make} of size {my_boat.engine_size} of color {my_boat.color} is {my_boat.year} years old and honk is"
      f" and can drop {my_boat.drop_anker()}")
