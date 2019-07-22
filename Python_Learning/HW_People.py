
# created my peoples class which contains the variable instances that will be attached when an object is created
class People():
     def __init__(self, first_name,last_name, dob, gender,nationality,id):
         self.firstname = first_name
         self.lastname=last_name
         self.dob = dob
         self.gender=gender
         self.nationality=nationality
         self.id=id


#created staff class and info list of passengers
class Staff(People):
    def __init__(self,first_name, last_name, dob, gender,nationality,id):
        super().__init__(first_name, last_name, dob, gender,nationality,id )

        self.info_passenger = []
        self.flight_list =[]

    def booking_passenger (self, passenger):
        self.info_passenger.append(passenger)


#Created a method to add flight details to a flight list

    def add_flights_list(self, flightlist):
        self.flight_list.append(flightlist)

class Passenger(People):

    def __init__(self, first_name, last_name, dob, gender, nationality, id, passport_number):
        super().__init__(first_name, last_name, dob, gender, nationality, id)
        self.passportnum = passport_number

    def get_details(self):
        return self.firstname + "," + self.lastname + "," + self.dob + "," +  self.gender + "," + self.nationality  + "," + self.id




#Assigned staff_01 as the object which gives the full name and id of the staff member
Dani =Passenger("Dani ","pegg", "4/1/1987","M","GB","01", "8629386")
staff1 =Staff("Di ","pg", "4/1/1987","M","GB","01")

staff1.booking_passenger(Dani)

print(staff1.info_passenger[0].get_details())

# #created the variables and inputed the data assigned to a passenger
# boss.bookingpassenger("Adam","Khyo","21/2/2089"," M","GB","234234")
# print(boss.info_passenger)
#
