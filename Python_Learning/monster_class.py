# here I will create my Monster class
   # add the attributes in the ___init___ mehtod
   # Add behaviors as individual methods


# constructor method to create an instance of monster
#monster3 = Monster("KOKO")

# class Monsters():
#
#     home = "cuba"
#     skills = []
#
#     # since this function is inside a class it is a method
#     def eat(self, food):
#         return "I nom nom " + food
#
#     def __init__(self, obj_name , age , height):
#         self.name = obj_name
#         self.age = age
#         self.height = height
#
#
#     def sleep(self):
#         return'zzz'
#
#     def add_skill(self, skill_arg):
#         self.skills.append(skill_arg)
#
#     def skills_in_interview(self):
#         skills_list = self.skills
#
#
#
# # To call sleep now. I needs an instance of monster
# # intialize - create an nsrance of monster using#
#
#
#
#
#
#
# monster1 = Monsters( "JJ",1, 1.90 )
# print(monster1.name)
# monster1.add_skill("SQL")
# print(monster1.skills)
# print(monster1.add_skill)
#
#
#
# print(monster1.home)
# monster1.home= "Russia"
# Monsters.home = "Japan"
# print(monster1.home)
# print(Monsters.home)
#



class Monster():
    def __init__(self):
        self.name = "Jullian"
        self.skill = "bend metal"

    def become_invisible(self):
     return "Learnt to be invisible "

    def change_color(self):
            return "Can become red, yellow and blue"

    def climb_doors(self):
            return " Can climb on doors 10ft tall "

    def sleep(self):
        return 'zzzz'
    def eat (self):
        return"nom nom"
    def scare (self):
        return "RAHHH"
    def scratch(self):
        return "claw claw"

monster1= Monster()
print(monster1.sleep())
