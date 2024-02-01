import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "store"
)
mycursor = mydb.cursor()

class Product:
    pass


