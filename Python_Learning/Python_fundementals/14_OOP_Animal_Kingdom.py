# What is inside class is called members
# one is a local variable -
# function inside a class is called methods. functions are outside a class
#

# def speak2(self): # This however, is not inside the class . It is in the file hence is now called a function/ D
#                   # functions are not used in OOP/classes

#Changing animal in memory not in the class


#Static

# When you create a class - class is a description and like a template - not used directly - describe what you want.
#Give me an example of this thing.

# class Animal:
#     animal_kind = "cow" # Local variable in the class
#
#     def speak(self): #This is inside a class hence it is a method
#         return "yum yum yum"
#
#     def speak(eat): #This is inside a class hence it is a method
#         return "#I like bones"
#
#     def speak2(): #This is inside a class hence it is a method
#         return "yum yum yum"
#
#print(Animal.animal_kind) #Why did this pass
#
# dog1 = Animal() # now I have an object of type animal # intiate line object
# dog2 =Animal()

#how object relate with class members
# print(dog1.speak()) # Object dog know this because of having self
# print(dog1.eat()) # object knows this so it works
#
# print(dog1.speak2()) #Object dog does not know this because of not having self - Does not have self so does not work



# print(Animal.speak()) # Animal does not know this because it has self
# print(Animal.speak2()) # Animal know this because it does not have self - Not working
#

#
#
# print(dog1.animal_kind)
# dog1.animal_kind = "Im a dog you id"
# print(dog1.animal_kind)
# print(dog1.speak2())
# print(Animal.animal_kind)
# Animal.animal_kind=  "Mouse"
# print(dog1.animal_kind)
#
# ferret = Animal()
# cat = Animal()
#
# print(cat.speak2())
# print(ferret.speak2())

# How does dog relate to members




#
# dog3 =Animal()
# #Using an object
# print(dog3.animal_kind)
# print(dog3.speak())
#
# #Object calling the dog can speak - part of the object - isolate it -
# print(dog3.speak())
# #can see animal kind but cannot speak - can hide - cant access it using the class - need an object to access it
# # Using the class
# print(Animal.speak())







class Animal:
    animal_kind = "cow" # Local variable in the class

    def speak(self): #This is inside a class hence it is a method
        return "yum yum yum"

    def speak(eat): #This is inside a class hence it is a method
        return "#I like bones"

    def speak2(): #This is inside a class hence it is a method
        return "yum yum yum"


turtle = Animal()
fish = Animal()

print(Animal.animal_kind)
print(turtle.animal_kind)
print(fish.animal_kind)

Animal.animal_kind ="spider"

Animal.animal_kind = "Spider"

print(Animal.animal_kind)
print(turtle.animal_kind)
print(fish.animal_kind)









# print(dog.animal_kind)
# print(dog2.animal_kind)
#
# dog2.animal_kind = "woff"
# print(dog.animal_kind)
# print(dog2.animal_kind)
# # This dog is now an object - object in memory
#
# # Difference with self key word

