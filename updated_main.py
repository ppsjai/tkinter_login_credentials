# Password Generator Project
# How de we provide credentials in that UI
# I have added JSON and exception handling in real time implementation for that create a (filename.json) to access the report in JSON format
# For exception handling i have created a different repository for and for more info see that file too
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle # instead of calling random.randint() we can use randint key alone
import pyperclip
import json

#TODO ---------------------------- PASSWORD GENERATOR ---------------------------------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "-", "+", "=", "-", "_", "~", "`",
               "{", "}", "[", "]", "|", ":", ";", ",", ".", "/", "?"]


    # list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))] # 8 yo 10 times
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]# 2 to 4
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]# 2 to 4

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list) # joins string together
    password_entry.insert(0, password)
    pyperclip.copy(password) # to copy entire password to our clipboard just we have to c+v that's it

#TODO ---------------------------- SAVE PASSWORD --------------------------------------------------------------- #
def save():
    domain = domain_entry.get()
    email = email_entry.get()
    password = password_entry.get() # it will open a pop up UI
    new_data = {
        domain: {
            "email": email,
            "password": password,
        }
    } # updated

    if len(domain) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any field empty.")
    # this else block has included of JSON to load an existing data in (filename.json),and add a data and update a data
    else:
        try:
            with open("json_report.json", "r") as file: # updated json file will create
                # json.load used to read JSON data from a file and convert it into a python object
                # Reading old data
                data1 = json.load(file)

        except FileNotFoundError:
            with open("json_report.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # to update any kind of info we can use json.update method
            # Updating old data with new-data
            data1.update(new_data)

            with open("json_report.json", "w") as file:
                # json.dump used to write python data in json file format
                # saving updated data
                json.dump(data1, file, indent=4)

        finally:
            domain_entry.delete(0, END)
            password_entry.delete(0, END)
            # now open UI and provide our credentials it will be described in our file.
            # to use delete key there are 2 types. first it start of the range and
            # last it use END key optional end of the range.

#TODO ----------------------------FIND PASSWORD-------------------------------------------------------------------#
# Updated-content have created a new function to find password for an existing domain with exception handling
def find_password():
    domain = domain_entry.get()
    try:
        with open("json_report.json") as file:
            data1 = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message="No Data File Found")
    else:
        if domain in data1:
            email = data1[domain]["email"]
            password = data1[domain]["password"]
            messagebox.showinfo(title=domain, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {domain} exist. ")
#TODO ---------------------------- UI SETUP ---------------------------------------------------------------------------- #
data = Tk()
data.title("PASSWORD MANAGER")
data.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# label
domain_label = Label(text="Domain name:")
domain_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
domain_entry = Entry(width=21)
domain_entry.grid(row=1, column=1)
domain_entry.focus() # focus the cursor into entry box
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jaikumar@gmail.com") # if we run our UI it will already inserted by my email
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#button
#I have included search button in this and recalling our function in command
search_button = Button(text="SEARCH", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
login_button = Button(text="LOG IN", width=36, command=save)
login_button.grid(row=4, column=1, columnspan=2)

data.mainloop()
