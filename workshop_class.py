# here I will create my Workshop class
   # add the attributes in the ___init___ mehtod
   # Add behaviors as individual method


# Behaviours of Workshop(methods)
# •	A Workshop should be able to list all attendees-->
# •	A Workshop should have a method to set_teacher-->
# •	A Workshop should have a method to add a monster to it's monster_attendees_list


#
# class Kworkshop():
#
#     monster_list = []
#
#     def __init__(self, name, name_worksp, teacher = 'not assigned'):
#       self.workshop_name= name
#       self.workshop_teacher = teacher
#       self.monster_list = []
#
#     def set_teacher(self, new_teacher):
#        self.workshop_teacher = new_teacher
#
#     def add_monster_to_list(self,monster):
#         self.monster_list.append(monster)
#
#     def list_attendees(self, attendee):
#         attendee_1 = self.monster_list(
#             counter =1
#             for attendee in attendee_1:
#         print(counter, '-', attendee)
#         #get list
#
#





#
# wrkshp1= Kworkshop('Scaring 6yr olds', "Scare 101", "")
# wrkshp1.workshop_teacher= "Ms S"
#
# print(wrkshp1.workshop_name)
# print(wrkshp1.workshop_teacher)
# print(wrkshp1.monster_list)
#
# wrkshp1.add_monster_to_list("zaid")
# wrkshp1.add_monster_to_list("Dick")
# wrkshp1.add_monster_to_list("Harry")
#
# print(wrkshp1.monster_list)
#


class Workshops():



    def __init__(self):
        self.name = "Master scaring class"
        self.set_teacher = "Ms Scary"
        self.attendees =(["Mike", "John","Dough"])

    def take_register(self):
        print(class1.attendees)

    def add_student(self, obj_name):
        self.attendees.append(obj_name)

    def set_teacher(self,name_teacher):
        self.set_teacher = name_teacher


class1 = Workshops()
print(class1.attendees)
print(class1.take_register())
print(class1.set_teacher)
print(class1.name)
class1.add_student("JJ")
print(class1.attendees)


