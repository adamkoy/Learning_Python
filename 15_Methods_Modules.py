# depends on what is passed into it - change the behavior - pass an object of that class - it will call on that calss/method
#Constructor = It is called automatically - use it to populate
#
# def speak(Animal):
#     return Animal.speak()"


    # def __init__(self): #called when the class has been intialized # special methods - just use it and system will look it
    #                              #Boiler code - python intrpreter to call that method  - color is different - intiate
    #     self.name = "Jimmy"

class Dog:
    animal_kind = "canine" #Global vs private local

    def __init__(self, obj_name, obj_breed, dog_age, owner): # Constructor method
        self.name = obj_name # Variable - what does self do? created a variable - parameter to change what the foh has
        self.breed = obj_breed
        self.age = dog_age
        self.owner = "Mark"
# Where I create the attributes for my future Objects


    def speak(self):
        return "bark"


# enter variables in my constructor which then passed into the contructor method
dog1 = Dog("Jimmy", "Bichon Frise", 12, "Dill")
dog2 = Dog("cindy", "Pitbull", 6)

print()
# Calling the objects out with the print method
print(dog2.name)
print(dog2.breed)
print(dog2.age)


# dog1 =Dog() # Python interpreter and puts it inside the obj.name
# dog2 =Dog("Jack2")
#
# print(dog1.name)
# print(dog2.name)
# print(__name__)
# print(Dog.__name__)