########################################################################################################

#This is the add function
def add(x,y):
    return x+y

add1 = str(add(2,4))
if add1 == '6':
    print('The add function is working. The total sum is' +' '+add1)

###########################################################################################################
#This is the subtraction function
def subtraction(x,y):
    return x-y
#########################################################################################################
print(subtraction(100,40)==60)
sub2 = str (subtraction(100,40))
if subtraction == False:
    print('The calculation did not work')
else:
    print('Well done, I can now subtract. The total sum is'+' '+sub2)
#########################################################################################################
#This is the multipy function
def multipy(x,y):
    return x*y

print(multipy(100,100))

###########################################################################################################
#This is the divide function
def divide(x,y):
    return x/y
print(divide(100,5))
############################################################################################################
#This is the area of a triangle space
def area_triangle(length, height):
    return (0.5 * length * height)

print('This is the area of your triangle')
print(area_triangle(10,100))
################################################################################################################

# inches to cm converter
def inch_2_cm (number,cm):
    return number*2.54

print(inch_2_cm(5,2.54))
print('Here is your conversion')
###################################################################################

#Tests
print(subtraction(10,2))
print(multipy(43,2))
print(divide(10,2))
#######################################################################################################################

# POKEMON CALCULATOR
import time

def evolve_pikachu(battle_points,evolution_stone):
    if '200' in battle_points and '1' in evolution_stone:
        return 'Raichu'
    else:
        return 'Sorry pikachu doesnt have enough points to evolve'

evolve1 = input("Do you want to attack Charazard?")
if evolve1 == 'yes':

    evolve2 = input('What attack do you want to intiate? 1) Electric punch 2) Shock Wave 3) Thunder Slash? Type 1,2,3 for your '
          'answer')

if evolve2 == '1':
    print("Pikachu smashed the hell out of charazard. You've earned 200 battle points!")
else:
    print("Your attack failed! Better luck next time, You've still earned 199 points!")

Evolve_time=input( "Enter your points earned").strip().lower()

if Evolve_time == '200' :
    print("Come quickly Pikachu is evolving.")
    time.sleep(2)
    print("Raichu is born!!!!!!!!!!!!!!")
else:
    print(evolve_pikachu('199','1'))
