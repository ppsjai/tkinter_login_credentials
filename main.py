# Password Generator Project
# how de we provide credentials in that UI
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle # instead of calling random.randint() we can use randint key alone
import pyperclip

#TODO ---------------------------- PASSWORD GENERATOR ---------------------------------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "-", "+", "=", "-", "_", "~", "`",
           "{", "}", "[", "]", "|", ":", ";", ",", ".", "/", "?"]

def generate_password():
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

    if len(domain) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=domain, message="These are the details entered:"
                                                      f" \nEmail: {email} \nPassword: {password} \nIs it ok to save")
        if is_ok:
            with open("login_report.txt", "a") as file:
                file.write(f"|{domain} | {email} | {password}\n")
                domain_entry.delete(0, END)
                password_entry.delete(0, END)
            # now open UI and provide our credentials it will be described in our file.
            # to use delete key there are 2 types. first it start of the range and
            # last it use END key optional end of the range.

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
domain_entry = Entry(width=35)
domain_entry.grid(row=1, column=1, columnspan=2)
domain_entry.focus() # focus the cursor into entry box
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "anymail@gmail.com") # if we run our UI it will already inserted by my email
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

#button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
login_button = Button(text="LOG IN", width=36, command=save)
login_button.grid(row=4, column=1)

data.mainloop()
