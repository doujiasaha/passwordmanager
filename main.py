from tkinter import *
from tkinter import messagebox
import random, string
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen():
    length = 16
    random_password = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    password_box.insert(END,random_password)
    pyperclip.copy(random_password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    
    website_input = website_box.get().title()
    user_input = name_box.get()
    password_input = password_box.get()
    new_data = {
        website_input: {
            "email": user_input,
            "password": password_input,
        }
    }
    
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Error", message="You've left some fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                #Read old data
                data = json.load(file) 
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updatin old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #Save updated data
                json.dump(data, file, indent=4)
        finally:
            website_box.delete(0,END)
            password_box.delete(0,END)

# ---------------------------- SEARCH ENTRY ------------------------------- #

def search_entries():
    website_input = website_box.get().title()
    try:
        with open("data.json", "r") as file:
            #Read old data
            data = json.load(file)
            #Updatin old data with new data
    except FileNotFoundError:
        messagebox.showinfo(title="No Entries yet", message="You currently do not have entries in your password manager.")           
    else:
        
        if website_input in data:
            user_data = data[website_input]["email"]
            password_data = data[website_input]["password"]
        
            messagebox.showinfo(title=website_input,message=f"Email: {user_data} \n"
                                f"Password: {password_data}")
        else:
            messagebox.showwarning(title=f"No Entry for {website_input}", message="No details for the website exists.") 
    

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
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

name = Label(text="Email/Username:")
name.grid(column=0,row=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

#Entries
website_box = Entry(width=18)
website_box.grid(column=1,row=1)
website_box.focus()

name_box = Entry(width=35)
name_box.insert(0, "john@doe.com")
name_box.grid(column=1,row=2, columnspan=2)

password_box = Entry(width=18)
password_box.grid(column=1,row=3)

#Buttons
search = Button(text="Search",command=search_entries ,width=12)
search.grid(column=2,row=1)

generate = Button(text="Generate Password", command=gen, width=12)
generate.grid(column=2,row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()