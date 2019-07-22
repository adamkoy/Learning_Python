
class Calculator():
    def __init__(self, type_of_cal): # this is a placeholder for values to pass
        self.type_of_calculator= type_of_cal

    def get_type(self):
       print(self.type_of_calculator)

    def Add(self, value1, value2):
       return value1 + value2   # better than - print(valu1+value2) # function should do one thing only - due to KISS

    def Subtract(self, value1, value2):
        return  value1-value2

    def Multiply(self,value1, value2):
        return value1*value2

    def Divide(self,value1,value2):
        return value1/value2

class Animal():
    def __init__(self, name,age):
        self.name=name
        self.age=age

