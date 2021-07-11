from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password_ = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_,

        }
    }
    if len(website) == 0 or len(password_) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any box empty.")
    else:
        messagebox.askokcancel(title=website,
                               message=f"These are the details entered : \n {email}  \n {password_}"
                                       f" \n "
                                       f"Is it ready to save ? ")
        try:
            with open("password.json", "r") as data:
                # Reading old data
                msd = json.load(data)
        except FileNotFoundError:
            with open("password.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data with new data
            msd.update(new_data)
            with open("password.json", "w") as data:
                json.dump(msd, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------- Find Password --------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("password.json") as data:
            dat = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data FIle Found")
    else:
        if website in dat:
            email = dat[website]["email"]
            password = dat[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email} \n Password : {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website} available .")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
# Canvas
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="My-logo.png")
canvas.create_image(100, 100, anchor="center", image=img)
canvas.grid(row=0, column=1)
# Label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
Email_label = Label(text="Email/Username")
Email_label.grid(row=2, column=0)
Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)
# Entry
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=63)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "williamskyle562@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
search = Button(text="Search", width=24, command=find_password)
search.grid(row=1, column=2)
generate_pass = Button(text="Generate Your unique Password", command=generate_password)
generate_pass.grid(row=3, column=2)
add = Button(text="Add", width=53, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
