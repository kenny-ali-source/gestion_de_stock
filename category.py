import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store"
)

class Category:
    def __init__(self, name):
        self.name = name

    def _create_category(self, name):
        mycursor = mydb.cursor()
        mycursor.execute("""
            INSERT INTO Category(name)
            VALUES(%s)
        """, (name,))
        mydb.commit()

    def _read_category(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Category")
        for (id, name) in mycursor:
            print(f"ID: {id}, Nom: {name}")

    def _update_category(self, id, name):
        mycursor = mydb.cursor()
        mycursor.execute("""
            UPDATE Category 
            SET name = %s
            WHERE id = %s
        """, (name, id))
        mydb.commit()

    def _delete_category(self, id):
        mycursor = mydb.cursor()
        mycursor.execute("""
            DELETE FROM Category 
            WHERE id = %s
        """, (id,))
        mydb.commit()


category_instance = Category(name="exemple")


category_instance._read_category()
category_instance._update_category(2, "Ali")
category_instance._delete_category(2)

   
