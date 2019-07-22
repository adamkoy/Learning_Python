


class Airplane():

    def __init__(self, brand,airline, num_passengers):
        self.brand = brand
        self.airline = airline
        self.num_passengers = num_passengers
        self.airplane_list = []

    def add_airplanes_list( self, airline, num_passengers):
        self.airplane_list.append(airline)
        self.airplane_list.append(num_passengers)


class Helicopter():
    def __init__(self, plane_member, company,heli_name , num_passengers):
        super().__init__(plane_member, company,)
        self.heli_name = heli_name
        self.num_passengers = num_passengers



airplane1 = Airplane("RR","EasyJet","300")
airplane1.add_airplanes_list("Easy Jet","300")
print(airplane1.airplane_list)
