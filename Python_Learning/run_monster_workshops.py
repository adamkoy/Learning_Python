# Run all the code in this file
# import needed classes
from monster_class import*
from workshop_class import*

#Create some workshops
#create some monsters



m1 = Monster()
#print("m1 can ", m1.name() and m1.scare() and  m1.sleep() and  m1.eat()))


m2= Monster()
m2.name= "Derek"
m2.breed = "Grooch"
print(m2.name)
print(m2.breed)
print("m2 can" , m2.skill)
m2= Monster()
print("m2 passed! "+ m2.climb_doors())
print("m2 passed! "+ m2.become_invisible())

see_me_nomore = Monster()
print(see_me_nomore.become_invisible())

rainbow_technique = Monster()
print(rainbow_technique.change_color())

rock_climber = Monster()
print(rock_climber.climb_doors())