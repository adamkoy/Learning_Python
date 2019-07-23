# connect python to northwind database
# use library Python ODBC

import pyodbc

class NwProducts():
    def __init__(self):
        self.server = 'localhost, 1433'  # local machine - your own machine - if you dont know the name
        self.database = 'NorthWind'
        self.username = 'sa'
        self.password =  ' Passw0rd2018'
        self.docker_Northwind = pyodbc.connect