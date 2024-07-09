from tkinter import *
from tkinter import ttk,messagebox
import main

root = Tk()
root.geometry("1000x780")
root.resizable(0,0)
root.title("Contacts Management System")


# Create frames
treeview_frame = Frame(root)
treeview_frame.place(x=20, y=10, width=980, height=600)

# Creating a Scrollbar
scrollbary = Scrollbar(treeview_frame, orient=VERTICAL)
scrollbary.pack(side=RIGHT, fill=Y)

# Create a style
style = ttk.Style()

# Setting a theme to ensure custom styles are applied correctly
style.theme_use("clam")

# Modify the Treeview style
style.configure("Treeview",
                background="#f0f0f0",
                foreground="black",
                rowheight=25,
                fieldbackground="#d9d9d9",
                font=("Helvetica", 11))

# Modify the Treeview heading style
style.configure("Treeview.Heading",
                background="#3b5998",   
                foreground="white",     
                font=("Helvetica", 14, "bold"))

# Modify the style for selected rows
style.map("Treeview", 
          background=[('selected', '#6b6b6b')],
          foreground=[('selected', 'white')])

# Create a Treeview widget
treev = ttk.Treeview(treeview_frame, height=30, yscrollcommand=scrollbary.set)
treev.pack()

# Adding the scrollbar
scrollbary.config(command=treev.yview, width=20)

# Create columns
treev['columns'] = ("Row Id","First Name","Last Name","Phone Number","Email Id")

# Set column widths
treev.column("#0", width=0, stretch=NO)
treev.column("Row Id", width=100, anchor=CENTER)
treev.column("First Name", width=200, anchor=CENTER)
treev.column("Last Name", width=200, anchor=CENTER)
treev.column("Phone Number", width=200, anchor=CENTER)
treev.column("Email Id", width=230, anchor=CENTER)

# Create headings
treev.heading("Row Id", text="Row Id", anchor=CENTER)
treev.heading("First Name", text="First Name", anchor=CENTER)
treev.heading("Last Name", text="Last Name", anchor=CENTER)
treev.heading("Phone Number", text="Phone Number", anchor=CENTER)
treev.heading("Email Id", text="Email Id", anchor=CENTER)

# Entry fields
id_label = Label(root, text="ROW ID: ")
id_label.place(x=20, y=650)
id_entry = Entry(root, width=10, font=("Helvetica", 10))
id_entry.place(x=80, y=650)

first_name_label = Label(root, text="FIRST NAME: ")
first_name_label.place(x=180, y=650)
first_name_entry = Entry(root, width=18, font=("Helvetica", 10))
first_name_entry.place(x=260, y=650) 

last_name_label = Label(root, text="LAST NAME: ")
last_name_label.place(x=400, y=650)
last_name_entry = Entry(root, width=18, font=("Helvetica", 10))
last_name_entry.place(x=480, y=650)

phone_no_label = Label(root, text="PHONE NUMBER: ")
phone_no_label.place(x=620, y=650)
phone_no_entry = Entry(root, width=18, font=("Helvetica", 10))
phone_no_entry.place(x=730, y=650)

email_label = Label(root, text="EMAIL ID: ")
email_label.place(x=180, y=690)
email_entry = Entry(root, width=40, font=("Helvetica", 10))
email_entry.place(x=245, y=690)

# Define functions
def add_contacts(First_Name, Last_Name, Number, Email):
    existing_contacts = main.show_contacts()
    for contact in existing_contacts:
        if contact[1] == First_Name and contact[2] == Last_Name and contact[3] == Number and contact[4] == Email:
            messagebox.showwarning("Warning", "Contact Already Exists!!!")
            return
    if First_Name == "" and Last_Name == "" and Number == "" and Email == "":
        messagebox.showwarning("Warning","Enter the required data")
    else:
        result = messagebox.askquestion("Confirm", "Are you sure you want to save this contact?")
        if result == 'yes':
            main.add_contacts(First_Name, Last_Name, Number, Email)
    show_contacts()


def update_contacts(id, First_Name, Last_Name, Number, Email):
    if id == "":
        messagebox.showwarning("Warning","Enter Row Id to update")
    else:
        result = messagebox.askquestion("Confirm", "Are you sure you want to update this contact?")
        if result == 'yes':
            main.update_contacts(id, First_Name, Last_Name, Number, Email)
    show_contacts()


def delete_contacts(id):
    if not treev.selection():
        messagebox.showwarning("Warning","Select data to delete")
    else:
        result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this contact?', icon="warning")
        if result == 'yes':
            curItem = treev.focus()
            contents = (treev.item(curItem))
            selecteditem = contents['values']
            treev.delete(curItem)
            main.delete_contacts(selecteditem[0])
    show_contacts()


def reset_entries():
    id_entry.delete(0, END)
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_no_entry.delete(0, END)
    email_entry.delete(0, END)

def show_contacts():
    global treev
    treev.delete(*treev.get_children())
    for i in main.show_contacts():
        treev.insert("", 'end', values=(i[0],i[1],i[2],i[3],i[4]))


# Buttons with custom styles
create_btn = Button(root, text="CREATE", width=12, height=1, command=lambda:add_contacts(first_name_entry.get(), last_name_entry.get(), phone_no_entry.get(), email_entry.get()), background='#4CAF50', foreground='white',relief=RIDGE)
create_btn.place(x=50, y=730)

update_btn = Button(root, text="UPDATE", width=12, height=1, command=lambda:update_contacts(id_entry.get(),first_name_entry.get(), last_name_entry.get(), phone_no_entry.get(), email_entry.get()), background='#FF9800', foreground='white',relief=RIDGE)
update_btn.place(x=200, y=730)

reset_btn = Button(root, text="RESET ALL", width=12, height=1, command=reset_entries, background='#2196F3', foreground='white',relief=RIDGE)
reset_btn.place(x=350, y=730)

delete_btn = Button(root, text="DELETE", width=12, height=1, bg="#cc0044", command=lambda:delete_contacts(id_entry.get()), background='#F44336', foreground='white',relief=RIDGE)
delete_btn.place(x=500, y=730)

show_contacts()
root.mainloop()
