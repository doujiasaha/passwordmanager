from tkinter import *
import random, string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen():
    length = 16
    random_password = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    password_box.insert(END,random_password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    
    website_input = website_box.get()
    user_input = name_box.get()
    password_input = password_box.get()
    
    with open("data.txt", "a") as file:
        file.write(f"{website_input} | {user_input} | {password_input} \n")

    website_box.delete(0,END)
    #name_box.delete(0,END)
    password_box.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0,row=1)

name = Label(text="Email/Username:")
name.grid(column=0,row=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

#Entries
website_box = Entry(width=35)
website_box.grid(column=1,row=1, columnspan=2)
website_box.focus()

name_box = Entry(width=35)
name_box.insert(0, "john@doe.com")
name_box.grid(column=1,row=2, columnspan=2)

password_box = Entry(width=18)
password_box.grid(column=1,row=3)

#Buttons
generate = Button(text="Generate Password", command=gen)
generate.grid(column=2,row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()