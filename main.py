import sqlite3
# Creating database and table
def create_table():
    conn = sqlite3.connect("Contacts.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Contact_Management (
                    First_Name text,
                    Last_Name text,
                    Number text,
                    Email text
                   )"""
                   )
    conn.commit()
    conn.close()


# Insert data into the table
def add_contacts(First_Name, Last_Name, Number, Email):
    conn = sqlite3.connect("Contacts.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM Contact_Management WHERE First_Name = '{First_Name}' AND Last_Name = '{Last_Name}' AND Number = '{Number}' AND Email = '{Email}'")
    result = cursor.fetchall()

    if len(result) == 0 and First_Name != "" and Last_Name != "" and Number != "" and Email != "":
        cursor.execute("INSERT INTO Contact_Management VALUES (?, ?, ?, ?)", (First_Name, Last_Name, Number, Email))

    conn.commit()
    conn.close()


# Delete data from the table
def delete_contacts(id):
    conn = sqlite3.connect("Contacts.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM Contact_Management WHERE rowid = '{id}'")

    conn.commit()
    conn.close()


# Update data in the table
def update_contacts(id, First_Name="", Last_Name="", Number="", Email=""):
    conn = sqlite3.connect("Contacts.db")
    cursor = conn.cursor()    

    if First_Name != "":
        cursor.execute(f"UPDATE Contact_Management SET First_Name = '{First_Name}' WHERE rowid = {id}")
    if Last_Name != "":
        cursor.execute(f"UPDATE Contact_Management SET Last_Name = '{Last_Name}' WHERE rowid = {id}")
    if Number != "":
        cursor.execute(f"UPDATE Contact_Management SET Number = '{Number}' WHERE rowid = {id}")
    if Email != "":
        cursor.execute(f"UPDATE Contact_Management SET Email = '{Email}' WHERE rowid = {id}")

    conn.commit()
    conn.close()

#Show data of the table
def show_contacts():
    conn = sqlite3.connect("Contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM Contact_Management")
    result = cursor.fetchall()

    conn.commit()
    conn.close()
    return result

create_table()
