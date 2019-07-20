#  function - functions are small and are testable -  get the best talent -
#Run blocks of code when called
#they should be unitary /small
#They can take in arguments

#function is like a machine.
     #it can take inputs
     #it can perform actions
     #it outputs different objects

#An arguement in a function like a variable that exists only in the scope of the function


#Syntax
# A function needs to be called to run it's code
# def_name_function(arg1,arg2):
       #runs block of code

#Good practices
#p functions should be unitary/ small jobs/ one job
# - arguements should have good names
#- functions should be used to keep your code DRY
     #DRY - Dont repeat yourself
# - functions should return NOT print


# def full_name():
#     print("Isabella Jones"
#
# full_name()

def say_hello():
    print("Hello there")
say_hello()


def full_name(f_name, l_name): #These arguments can only be used inside the block of code
    full_name_var = f_name+ " " + l_name # using a variable to hold both of the names
    return full_name_var

print(full_name("Hamza", "Daniel"))