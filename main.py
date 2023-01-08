import tkinter
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- UI SETUP ------------------------------- #


def save():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please check for empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You are about to save the following: \nEmail: {email} \nPassword: {password} \n")
        if is_ok:
            with (open("data.txt", "a")) as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_field.delete(0, END)
                password_field.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas = Canvas(width=200, height=200, highlightthickness=3)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
website_field = Entry(width=35)
website_field.focus()
website_field.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_field = Entry(width=35)
email_field.insert(END, "roman@me.com")
email_field.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_field = Entry(width=21)
password_field.grid(column=1, row=3)

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)





















window.mainloop()
