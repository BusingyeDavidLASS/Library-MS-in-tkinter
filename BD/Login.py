from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

# Function to authenticate user login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Retrieve user credentials from the database
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user is not None:
        messagebox.showinfo("Success", "Login successful!")
        close_button.config(state=NORMAL)  # Enable the close button
        signup_link.config(state=NORMAL)  # Enable the sign-up link
    else:
        messagebox.showerror("Error", "Invalid username or password")
    
    conn.close()

# Function to close the window
def close_window():
    window.destroy()

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Function to handle login on pressing Enter key
def on_enter(event):
    login()

# Function to ignore window closing event
def on_closing():
    window.mainloop()

# Function to open the sign-up page
def open_signup():
    # Get the current directory
    current_dir = os.path.dirname(__file__)
    # Path to the sign-up page script (assuming it's named 'signup_page.py')
    signup_page_path = os.path.join(current_dir, 'Signup.py')
    
    # Check if the sign-up page script exists
    if os.path.exists(signup_page_path):
        # Run the sign-up page script
        os.system('python ' + signup_page_path)
    else:
        messagebox.showerror("Error", "Sign-up page script not found")

# Main Tkinter window
window = Tk()
window.title("Login")
window.geometry('500x500')
window.configure(bg='#333333')

# Intercept window closing event
window.protocol("WM_DELETE_WINDOW", on_closing)

# Creating widgets
frame = Frame(window, bg='#333333')
frame.pack(expand=True)

login_label = Label(frame, text="Login Page", bg='#333333', fg="#315257", font=("Arial", 30))
username_label = Label(frame, text="Username", bg='#333333', fg="#315257", font=("Arial", 16))
password_label = Label(frame, text="Password", bg='#333333', fg="#315257", font=("Arial", 16))

username_entry = ttk.Entry(frame, font=("Arial", 16))
password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))

show_password_var = IntVar()
show_password_check = Checkbutton(frame, text="Show Password", variable=show_password_var, bg='#333333', fg="#315257", font=("Arial", 12), command=toggle_password)

login_button = Button(frame, text="Login", bg="#315257", fg="#FFFFFF", font=("Arial", 16), command=login)
close_button = Button(frame, text="Continue", bg="#315257", fg="#FFFFFF", font=("Arial", 16), command=close_window, state=DISABLED)  # Initially disabled
signup_link = Button(frame, text="Sign Up", bg="#315257", fg="#FFFFFF", font=("Arial", 16), command=open_signup)


# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, pady=(20, 0))
username_entry.grid(row=1, column=1, pady=(20, 0), padx=10, ipady=7, sticky="ew")
password_label.grid(row=2, column=0, pady=(20, 0))
password_entry.grid(row=2, column=1, pady=(20, 0), padx=10, ipady=7, sticky="ew")
show_password_check.grid(row=3, column=0, columnspan=2, pady=10)
login_button.grid(row=4, column=0, padx=(40, 10), pady=30, sticky="ew")
close_button.grid(row=4, column=1, padx=(10, 40), pady=30, sticky="ew")
signup_link.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

# Bind the Enter key to the login function
password_entry.bind('<Return>', on_enter)

window.mainloop()
