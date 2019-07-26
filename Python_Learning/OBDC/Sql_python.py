#connect python to northwind database
# use library Python ODBC

import pyodbc

class NwProducts():
    def __init__(self):
        self.server = 'localhost, 1433'  # local machine - your own machine - if you dont know the name
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' + 'SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

# print(result)
# receives a Cursor when it connects which directs you - use it to read write etc



def create(self):
    self.cursor.execute(' CREATE TABLE RBS_Customers (Name_id Int, F_name varchar(20), L_name varchar(20))')
    self.cursor.commit()

def insert(self):
    self.cursor.execute(' INSERT INTO RBS_Customers (   1 ,   ,   )      VALUES (1, Adam, Koyuncu        ')
    self.cursor.commit



def read (self):
    result =self.cursor.execute(" SELECT * FROM PRODUCTS")
    rows = result.fetchall()
    for row in rows:
        print(row.ProductID, row.ProductName)

#



#Cursor is a handle which you where you pass the ????
#Here I am calling the cursor handle and calling the sql and saving it in the variable
# opening and clossing of a method - receives a sql as a paramenter which will execute      result saved in the variable

 # inside the result set is a matrix - fetchall -

#23 calling the execute method of the cosa object and
#]passing a sql statement to from the database and saving the result set saved in results




my_db = NwProducts("")
result = my_db.cursor.execute("select * from Products")
rows = result.fetchall()
for row in rows:
    print(row.ProductID, row.ProductName)


    # one class with four methods CRUD

    def add_name(self,database_file, new_person):
        query = "INSERT INTO Person VALUES (?, ?, ?);"

        self.cursor.execute(query, list(new_person))
        self.cursor.close()
        self.connection.close()


    def get_name(self, database_file, table_name, person_id):
        query = "SELECT "+ ','database_file+',' || ' ' || ',' + table_name FROM Person WHERE id=?;"




# finally - use of memory = need to pit it under a try block - beyound the power of the programmer =
#make sure the user satisfies the user -
# wrap code in protections which is a try.
# give another try using except = when done with wap we need to close it.
# not freeing the resource
# finally - it allows to close and not take resources from computer



# function is not a type - a type is your own thing - there is no such thing as Northwind
# creating your own type - create own class with the attributes and actions own employee can do
# create a database thing. i'm going to call this thing northwind -
# Python doesnt know what it is so we describe it. It will have propteries password - docker and put values inside it.
#what will this thing do? Describe your own thing.
# the class I described called northwind - I want to use it - give me one in memory that I can use hacker = Northwind
#give me one instance of nortwind class and place it into an object
#  mydb.create - at that point we run the method

# OOP you create objects and you call methods.