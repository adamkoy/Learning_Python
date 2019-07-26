# connect python to northwind database
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



my_db = NwProducts()
result = my_db.cursor.execute("select * from Products")
# receives a Cursor when it connects which directs you - use it to read write etc
rows = result.fetchall()
for row in rows:
    print(row.ProductID, row.ProductName)



# create , update and alter , CRUD



