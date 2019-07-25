# Python IO  = Input or Output for file handling
#If program does not have permission to open the file, it will not open.
# need to wrap them in try and exception code
#denial of service


#This result is not the file - it is a pointer object to the file - call the object to retrieve the value inside.


try:
    file = open(".Order.txt2", "a")  # use open function to open binary file - a flag and w (overides) flag

except FileExistsError as erromsg:
    print(" Something wrong occured" ,erromsg)

except FileNotFoundError as erromsg:
    print(" Something wrong occured" ,erromsg)


# inside result there is a field called content - to get access to consent - call the method to acess the variable
# r = to read  - a - leaves it w - overwrites

def file_opener(file):
    try:
        result = open(file,"r")
        list_lines = result.readlines()
        for line in list_lines:
            #print(line.rstrip('/n'))
            print(line+"\n")
            result.close()


            #print(line)# it will need to go inside a loop
    except ValueError as msg:
        print("something occured", msg)
    except FileExistsError as errmsg:
        print("Something went wrong, fix again")





#
# def file_writer(file):
#     try:
#         result = open(file,"w")
#         list_lines = result.write("Another weed crime444")
#
#     except ValueError as msg:
#             print("something occured", msg)
#     except FileExistsError as errmsg:
#             print("Something went wrong, fix again")
#
#
# file_writer("my_file1.txt1")
# file_opener("my_file1.txt1")
#

class My_file_hacker ():
    def __init__(self,value, file, text):
        self.value= value
        self.file = file
        self.text = text

    def file_writer(self,file, value, text):
        try:
            result = open(file, value )
            list_lines = result.write(text)

            result.close()
        except ValueError as msg:
            print("something occured", msg)
        except FileExistsError as errmsg:
            print("Something went wrong, fix again")



    def file_reader(self, file, value):
        try:
            result = open(file ,value)
            print(result.readlines())
            result.close()

        except ValueError as msg:
            print("something occured", msg)
        except FileExistsError as errmsg:
            print("Something went wrong, fix again")



hacker1 = My_file_hacker ("my_file1.txt1", "w", "You've been hacked")

hacker1.file_writer("my_file1.txt1", "w", "you've been smacked")
hacker1.file_reader("my_file1.txt1", "r")