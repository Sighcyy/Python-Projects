import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


#Password Generator Project
def generate_password():
    password_textbox.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_textbox.insert(0,password)
    pyperclip.copy(password)




def save():

    website = website_textbox.get()
    email = email_username_textbox.get()
    password = password_textbox.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError) :
            data = new_data
        else:
            data.update(new_data)
        finally:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            website_textbox.delete(0, "end")
            password_textbox.delete(0, "end")




def find_password():
    website = website_textbox.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "No details for website")

window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, background="white")




canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
myPhoto = tkinter.PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=myPhoto)
canvas.grid(row=0, column=1)


website_label = tkinter.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_textbox = tkinter.Entry(width=30)
website_textbox.grid(row=1, column=1, columnspan=1)
website_textbox.focus()
website_search_button = tkinter.Button(text = "Search", command = find_password)
website_search_button.grid(row=2, column=0)
website_search_button.grid(row=1, column=2, columnspan=2)



email_username_label = tkinter.Label(text="Email/Username:", bg="white")
email_username_label.grid(row=2, column=0)
email_username_textbox = tkinter.Entry(width=40)
email_username_textbox.grid(row=2, column=1, columnspan=2)
email_username_textbox.insert(0, "dummy.email@gmail.com")

password_label = tkinter.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
password_textbox = tkinter.Entry(width=23)
password_textbox.grid(row=3, column=1,  columnspan = 1)
password_generate_button = tkinter.Button()
password_generate_button.configure(text="Generate Password", bg="white", command= generate_password)
password_generate_button.grid(row=3, column=2)


add_password_button = tkinter.Button()
add_password_button.configure(text="Add", width=35, bg="white", command = save)
add_password_button.grid(row=4, column=1, columnspan=2)







window.mainloop()
