
# created my peoples class which contains the variable instances that will be attached when an object is created
class People():
     def __init__(self, full_num, dob, gender,nationality):
         self.fullnam = full_num
         self.dob = dob
         self.gender=gender
         self.nationality=nationality


#created staff class and info list of passengers
class Staff(People):
    def __init__(self,full_name, dob, gender,nationality, staff_id):
        super().__init__(full_name, dob, gender,nationality )
        self.full_name = full_name
        self.staff_id= staff_id
        self.info_passenger = []
        self.flight_list =[]

#Use the append method to add a passenger's details into the info_passenger_list
    def bookingpassenger(self,pfull_name,dob, gender,nationality,__passport_num):
        self.info_passenger.append(pfull_name)
        self.info_passenger.append(dob)
        self.info_passenger.append(gender)
        self.info_passenger.append(nationality)
        self.info_passenger.append(__passport_num)


#Created a method to add flight details to a flight list

    def add_flights_list(self, flightlist):
        self.flight_list.append(flightlist)


#Assigned staff_01 as the object which gives the full name and id of the staff member
boss =Staff("Dani pegg", "4/1/1987","M","GB","01")

#created the variables and inputed the data assigned to a passenger
boss.bookingpassenger("Adam Khyo","21/2/2089"," M","GB","234234")
boss.bookingpassenger("Sarah Reiner","4/2/2039"," F","GB","23449784")
print(boss.info_passenger)
