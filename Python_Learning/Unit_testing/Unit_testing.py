
from Simple_calculator import Calculator


# Unit testing - testing a small piece of your code - function of 3-5 lines - smallest unit of code - method - function
# Ensure the code is working/ quailty control/
# You gave the input and you know what you expected - pass it inside and compare what you have with the function 2+2
# What you pass in , what you expect - proper framework
#
#
# TDD - brain storm requirement - pick small feature and make a test to see if the software is working - will fail.
# Design and done the analysis. test first and code after.

# 1 variable which can be changed - reassign it easier. Always code with having variables holding the values

#2 hard coded - its fixed need to change it all the time - avoid if possible
#calc is a box for calculator

type_of_calculator =  "Standard" #1
calc = Calculator(type_of_calculator)  #2
calc.get_type()

result = calc.Add(2,3)

print(result)

result = calc.Subtract(10,2)
print(result)

result = calc.Multiply (10,20)
print(result)
#cal