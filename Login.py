import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('500x500')
window.configure(bg='#333333')

def login():
    username = "admin"
    password = "admin"
    if username_entry.get()==username and password_entry.get()==password:
        window.destroy()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')
#edit the entry boxes to make th
# Creating widgets
login_label = tkinter.Label(
    frame, text="Login Page", bg='#333333', fg="#315257", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#315257", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#315257", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#315257", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()