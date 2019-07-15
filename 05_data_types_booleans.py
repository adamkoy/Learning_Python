# Booleans
#Boolean is a data type that is either truwe and false

#Syntax is capital letter
var_true = True
var_false= False

print(type(var_true))
print(type(var_false))

# When we equate /evaluate something we get a boolean as a response
#Logical operators return boolean
#== / != / <> />= /<=

weather = 'Rainy'
print(weather =='Sunny')
print(weather =='Rainy')

#Logical **AND**  & **OR**
#Evaluate two sides, and BOTH have to be true for it to return True
print(True and False)
print(weather == 'Rainy' and weather == 'Sunny')

print(weather == 'Rainy' and weather == 'Rainy')
print(True and True)

#Logical OR - One of the side of the equasion have to be True to return True
print('>Testing logical or:')
print(True or False)
print(False or False)

#Some methods or functions can return booleans
potential_number = '10'
print('hey')
print(potential_number.isnumeric())
print('Location in code 2!')
text = 'Hello world!'
print(text[0] == 'H')
print(text.startswith('H'))
print(text.startswith('h'))

print('Testing .endswith(arg)')
print(text[-1] == '!') # String are a list of characters. -1 represents the last index in the said list
print(text.endswith('!'))
print(text.endswith('?'))


#Booleans and numbers - anything that is above 1 is Treu
print("printing bool values of numbers")
print(bool(0))
print (bool(13))
print (bool(1))
print (bool(1+3j))
print(bool(3.14))

#Value of none
print(bool (None))
