# # Data types
# # #Computers are stupid
# # They dont understand context, and we need to be specific with data types
#
# # We can use type() to check datatypes
# # Strings
#   # List of Characters bundled together in a specific order
#
# print('hello')
# print(type('hello'))
#
# # concatination of strings - joining of two strings
# string_a = 'hello there'
# name_person = 'Juan Peter'
# print(string_a+''+name_person)
#
# # Useful methods
# #Lenght
# print (len(string_a))
# print (len(name_person))
#
# #Strip
# # Removes training white spaces
#
# string_num=' 09389 '
# print (type(string_num))
# print (string_num)

# print(string_num.strip())

#.Split it is a method for strings
# it splits into a specific location and output a list (datatype)
string_text = "Hello, my name is Filipe, I like turtle"
split_string = string_text.split(', ')
print(split_string)

#count /lower/Upper / Capitalize

text_example =  "Here is some tExt, with lot's of Text"
print(text_example.count('e'))
print(text_example.count('tExt'))

#Lower
print(text_example.lower())

#Upper
print(text_example.upper())

#Capitalize
print(text_example.capitalize())
print('PizzaHut'.capitalize())
print('PIZZAHUT'.capitalize())
print('pizza hut'.capitalize())
#
#
# print('please give us a string to print')
#
#
#
# user_input_first_name = input('What is your first name?')
# print(user_input_first_name)
# #Casting
# #Get user input / first name
# first_name = input ('what is your first name?')
# #Save user input to variable
# #Get user last name
# last_name = input ('what is your last name?')
# # Join the two and
# # let us use concatination
# full_name = first_name +' '+last_name
# print(full_name)
# # Lets us use interpolation = can use variable inside the string
# welcome_message = f"Hello {full_name}, you are very welcome!"
# print(welcome_message)
#
#
#
#
