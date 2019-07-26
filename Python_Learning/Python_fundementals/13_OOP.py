class Calculator():

    def add(num1,num2):
     return num1+num2

    def sub(num1,num2):
      return num1-num2

    def multiply(num1,num2):
      return num1*num2

    def divide(num1,num2):
      return num1/num2

    value1 = int(input('Enter the first value'))
    value2= int(input('Enter the second value'))

    result = add(value1,value2)
    print("The result is", result)

#the value that has been set inside is a local variable. It does not change.
def AreaOfCircle(radius):
    PI = 3.142
    area = PI * radius *radius
    return area

result = AreaOfCircle(int(input("Please enter your circle radius")))
print(result)


#
# value1 = 5+5
# print(value1)
#
#
# value2 = 6-5
# print(value2)
#
# #// will not recongize floats
# value3 = 7/2
# print(value3)
#
# value4 = 8+8
# print(value4)
#
# def add()