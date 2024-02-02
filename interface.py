import mysql.connector
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Gestion de stock")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Gestion de stock"

def reverse(tuples):
    return tuples[::-1]

def insert(name, price, quantity, description):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="store")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255),
                description TEXT,
                price INTEGER,
                quantity INTEGER,
                id_category INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255)
            )
        """)

       
        cursor.execute("INSERT INTO Product (name, price, quantity, description, id_category) VALUES (%s, %s, %s, %s, %s)",
                       (name, price, quantity, description, 1)) 

        conn.commit()
        conn.close()
        print("Insertion réussie")
    except Exception as e:
        print(f"Error in insert: {e}")


def delete(data):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="store")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM product WHERE id = %s", (data,))

        conn.commit()
        conn.close()
        print("Suppression réussie")
    except Exception as e:
        print(f"Error in delete: {e}")

def update(name, price, quantity, idName):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="store")
        cursor = conn.cursor()

        cursor.execute("UPDATE product SET name = %s, price = %s, quantity = %s WHERE id = %s",
                       (name, price, quantity, idName))

        conn.commit()
        conn.close()
        print("Mise à jour réussie")
    except Exception as e:
        print(f"Error in update: {e}")

def read():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="store")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM product")
        results = cursor.fetchall()

        conn.close()
        return results
    except Exception as e:
        print(f"Error in read: {e}")

titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Arial bold', 15))
nameLabel = Label(root, text="Name", font=('Arial bold', 15))
priceLabel = Label(root, text="Price", font=('Arial bold', 15))
quantityLabel = Label(root, text="Quantity", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
priceLabel.grid(row=3, column=0, padx=10, pady=10)
quantityLabel.grid(row=4, column=0, padx=10, pady=10)

entryId = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryPrice = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryQuantity = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryPrice.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryQuantity.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

def insert_data():
    itemName = str(entryName.get())
    itemPrice = str(entryPrice.get())
    itemQuantity = str(entryQuantity.get())
    itemDescription = "votre_description"  # Ajoutez votre valeur de description

    if itemName == "" or itemPrice == "" or itemQuantity == "":
        print("Erreur: Remplissez tous les champs")
        return

    insert(itemName, itemPrice, itemQuantity, itemDescription)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result[0], text="", values=result[1:], tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = int(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result[0], text="", values=result[1:], tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_item = my_tree.selection()[0]
    update_id = int(my_tree.item(selected_item)['values'][0])
    update(entryName.get(), entryPrice.get(), entryQuantity.get(), update_id)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result[0], text="", values=result[1:], tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=result[0], text="", values=(result[0], result[1], result[2], result[3]), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()
