from HW_Airports import *

class Airplane(Aircraft):

    def __init__(self, plane_member, company, flight_time):
        super.__init__(plane_member,company)
        self.plane_member = plane_member
        self.company = company
        self.flight_time = flight_time


class Helicopter(Aircraft):
    def __init__(self, plane_member, company,heli_name ):
        super().__init__(plane_member, company,)
        self.heli_name = heli_name

