# Encapsulation
#
# It is considered standard or best practice to keep internal data or attributes as private
#as possible. Only a class should be able to have access to internal variables
# No access form outside# security risk if you can go and change the variables.#memoryt protects the object.
#Only defence is getters and setters
#Want to control access to that variable -
class Person():

    def __init__(self, age, name,email, height):
     self.set_height( height) # pyhton calls it _Person__height
     self.age =age
     self.name = name
     self.email = email

    def show(self):
        #self.__height= 50
        print(f"My name is {self.name} and I am {self.age} old amd my email is {self.email}, {self.__height}")

    def set_height(self,value):
        if value > 9 or value < 0:
         self.__height = 4.5
        else:
            self.__height = value

    def get_height(self):
         return self.__height



markson = Person (25,"Markson","joe@done.com", 1.79)
#markson.show()
#markson.name ="Filipe"
#markson.show()
#markson.__age = 30
#print(markson.age)
markson._Person__height = 60 # python on hides from accidental outside change not in intentional
markson.show()
##print(markson.__height) # This will crach
#print(markson._Person__height)# This will not
markson.set_height(200)
markson.show()
print(markson.get_height())