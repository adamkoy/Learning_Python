import time

#For Loops in Python
# used to iterate over collections. Lists and dictionaries

#placeholder is a variable that its scope is limited to the loop - the value will be stored in the placeholder for that
# loop
#Syntax
# for <placeholder> in <list>:
  #run block of code

#x_crazy_landlords = ["Cruella de vill","Donald Duck","Popeye the Maltese"]
#
#
# counter = 0
#
# for land in x_crazy_landlords:
#     print("hello")
#     print(land)
#     print(counter)
#     time.sleep(5)
#     counter += 1
#

#Exercise 1=-//
#Print the name of our landlords with nice formating
# Listing them using numbers


x_crazy_landlords = ["Cruella de vill","Donald Duck","Popeye the Maltese"]

counter = 1
for land_lord in x_crazy_landlords:
    print(counter,"-", land_lord)
    counter+=1


## Further loops
#
# list_data = [1,2,3,4,5,]
# embeded_list = [[1,2,3,],[5,6,7]]
#
# # for num in list_data:
# #     print(num)
#
# for data in embeded_list:
#  print(data)
#  for number in data:
#        print(number)
#        time.sleep(2)
#
#
# #################################################################################WRONG##############
# team_sparta = ["Shav", "Hamza","Payal", "Ally", "Omid","Daniel", "Zaid","Muji" ,"Adam", "Matt"]
# losing_lego_team = [["Zaid", "Hamza","Shav","Omid","Shav"]]
#
# for people in team_sparta:
#     print(people)
#
#     for losing_team in people:
#         print(losing_team)

##############################################################################################REDO ##

list_names = ["Jojo", "Albert","Linda", "Bob", "Prince", "Will"]
#
# for names in list_names:
#     print('Hello', names)
#

list_scores = [1, 10, 3, 4, 5, 6]
for num in list_scores:
 result_percent = num / 10 *100
print(result_percent)

#
# list_embeded_scores =[[10,5,2],[3,4,6]]
#
# for ind_list in list_embeded_scores:
#     print(ind_list)
#     for num in ind_list:
#         print(num*2)