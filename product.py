import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store"
)

class Product:
    def __init__(self, name, description, price, quantity, id_category):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.id_category = id_category

    def _create_product(self):
        mycursor = mydb.cursor()
        mycursor.execute("""
            INSERT INTO Product(name, description, price, quantity, id_category)
            VALUES(%s, %s, %s, %s, %s)
        """, (self.name, self.description, self.price, self.quantity, self.id_category))
        mydb.commit()

    def _read_product(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Product")
        for (id, name, description, price, quantity, id_category) in mycursor:
            print(f"ID: {id}, Nom: {name}, Description: {description}, Price: {price}, Quantity: {quantity}, id_category: {id_category}")

    def _update_product(self, id, name, description, price, quantity):
        mycursor = mydb.cursor()
        mycursor.execute("""
        UPDATE Product 
        SET name = %s,
            description = %s,
            price = %s,
            quantity = %s                
        WHERE id = %s
    """, (name, description, price, quantity, id))
    mydb.commit()

    def _delete_product(self, id):
        mycursor = mydb.cursor()
        mycursor.execute("""
            DELETE FROM Product 
            WHERE id = %s
        """, (id,))
        mydb.commit()


product_instance = Product(name="example", description="description", price=20, quantity=50, id_category=1)

product_instance._create_product()
product_instance._read_product()
product_instance._update_product(2, "Ali")
product_instance._delete_product(2)
