# # #Lists and Dictionaries
# # #List
# #
# # #Sometimes we just need to list our crazy pokemons ;)
# # # because we dont eant to work there
# #
# # #This is how you make a list
# # # [] separate items ,
# # #['bananas', 'pineapple', 'gasoline']
# # #declaring a list and saving to a variable
# #
# # crazy_pokemons = ['Snorlax', 'Jigglipuff', 'Mewtoo']
# # print(crazy_pokemons)
# # print(type(crazy_pokemons))
# #
# # #List are organized using index
# # # [0 ,1 ,2 ]
# # # [-3,-2 ,-1 ]
# # #['bananas', 'pineapple', 'gasoline']
# # #indexes start at 0
# #
# # print(len(crazy_pokemons))
# # print(crazy_pokemons[2])
# # print(crazy_pokemons[0])
# # #If you want to print the last in the list
# # #you have two options
# #   # array [len (array) - 1] or
# #   #
# #
# # print(crazy_pokemons[len(crazy_pokemons)-1])
# # print(crazy_pokemons[-1]) # Gives out Mewtoo
# #
# #   # Re-assigning the value in a list, using the index
# #   # We need to evolve Metwoo to Mewtree
# #
# # crazy_pokemons[2] = 'Mewtree'
# # print(crazy_pokemons)
# #
# # #Appending a new pokemon
# # #We caught a pigeoto # Adds into the array list
# #
# #
# # crazy_pokemons.append('Pigeoto')
# # print(crazy_pokemons)
# #
# # crazy_pokemons.insert(0, 'Ratata') # Can insert into specific index
# # print(crazy_pokemons)
# #
# #
# # # Removing a record
# # crazy_pokemons.pop()# Removes the last one when blank
# # print(crazy_pokemons)
# #
# # crazy_pokemons.pop(0)
# # print(crazy_pokemons)
# #
# # # Filtering and getting things out with specific names -
# # # Want to remove Mewtree
# #
# # crazy_pokemons.remove('Ratata')
# # print(crazy_pokemons)
# #
# # crazy_pokemons.insert(2,'Ratata')
# # crazy_pokemons.insert(2,'Ratata')
# # crazy_pokemons.insert(2,'Ratata')
# # print(crazy_pokemons)
#
# # List can have any datatypes
#
# mixed_list =[ 'Jones',10,42,'John']
# print(mixed_list)
# print(type(mixed_list[0]),type(mixed_list[1]))
#
# #Inception List
#
# leo_d = ['first', 2,['leo','d']]
#    # [o ,1 ,2  ]
# print(leo_d[0][2])
# print('accessing the index 2')
# print(leo_d[2])
#
# sub_array = leo_d[2]
# print(sub_array)
# print(sub_array[1])
#
# #All of this is the same as
# print(leo_d[2][0][1])
#
# #Accessing leo instead of d
# print(leo_d[2][1])
# print(leo_d[2][0][1])


#--------------------------------------------------------------------------------------------

# Tuples
# Tuples are immutable lists
#Meaning they do not change
#Syntax is as follows
   # tuple_list = ('hello', 10, 13, 4)
# Working with impeded and inception

my_tuple = ('eggs' , 'bread' ,'oats', [11, 12])
print(my_tuple)
print(type(my_tuple))

breakpoint()
# We cannot change the tuple itself , but we cqn change the state of items inside.
# Re cannot reassign them