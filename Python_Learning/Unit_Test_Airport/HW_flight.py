from HW_People import*


class Flights():
    def __init__(self,origin, destination, date, time):
        self.origin= origin
        self.destination= destination
        self.date=date
        self.time=time



route11 = Flights("origin","Italy","12/3/2020", "00:44")
boss.add_flights_list("route11")
print(boss.flight_list)
