#  Create an Airport


# created my peoples class which contains the variable instances that will be attached when an object is created
class People():
     def __init__(self, full_num, dob, gender,nationality):
         self.fullnam = full_num
         self.dob = dob
         self.gender=gender
         self.nationality=nationality


#created staff class and info list of passengers
class Staff():
    def __init__(self,full_name, staff_id):
        self.full_name = full_name
        self.staff_id= staff_id
        self.info_passenger = []
        self.airplane_list = []
        self.flight_list =[]
#Use the append method to add a passenger's details into the info_passenger_list
    def bookingpassenger(self,pfull_name,dob, gender,nationality,passport_num):
        self.info_passenger.append(pfull_name)
        self.info_passenger.append(dob)
        self.info_passenger.append(gender)
        self.info_passenger.append(nationality)
        self.info_passenger.append(passport_num)


    def add_flights_list(self, flightlist):
        self.flight_list.append(flightlist)


#Assigned staff_01 as the object which gives the full name and id of the staff member
boss =Staff("Dani", "id11")

#created the variables and inputed the data assigned to a passenger
boss.bookingpassenger("Adam Khyo","21/2/2089"," M","GB","234234")
boss.bookingpassenger("Sarah Reiner","4/2/2039"," F","GB","23449784")
print(boss.info_passenger)



#created an aircraft class where I give two attributes. This will be the superclass



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



airplaneboss = Airplane("RR","EasyJet","300")
airplaneboss.add_airplanes_list("Easy Jet","300")
print(airplaneboss.airplane_list)


class Flights():
    def __init__(self,origin, destination, date, time):
        self.origin= origin
        self.destination= destination
        self.date=date
        self.time=time



route11 = Flights("origin","Italy","12/3/2020", "00:44")
boss.add_flights_list("route11")
print(boss.flight_list)

