import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Function to create SQLite database
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 username TEXT PRIMARY KEY,
                 password TEXT)''')
    conn.commit()
    conn.close()

# Function to sign up a new user
def sign_up(event=None):
    username = username_entry.get()
    password = password_entry.get()

    # Check if username or password is empty
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone() is not None:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        conn.close()
        return

    # Insert the new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Sign up successful. You can now log in.")
    window.destroy()


# Function to close the window
def close_window():
    window.destroy()

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Main Tkinter window
window = Tk()
window.title("Sign Up")
window.geometry('500x510')
window.configure(bg='#333333')

# Create SQLite database
create_database()

# Creating widgets
frame = Frame(window, bg='#333333')
frame.pack(expand=True)

signup_label = Label(frame, text="Sign Up", bg='#333333', fg="#315257", font=("Arial", 30))
username_label = Label(frame, text="Username", bg='#333333', fg="#315257", font=("Arial", 16))
password_label = Label(frame, text="Password", bg='#333333', fg="#315257", font=("Arial", 16))

username_entry = ttk.Entry(frame, font=("Arial", 16))
password_entry = ttk.Entry(frame, show="*", font=("Arial", 16))

signup_button = Button(frame, text="Sign Up", bg="#315257", fg="#FFFFFF", font=("Arial", 16), command=sign_up)

show_password_var = BooleanVar()
show_password_check = ttk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password)

# Placing widgets on the screen
signup_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_label.grid(row=1, column=0, pady=(20, 0))
username_entry.grid(row=1, column=1, pady=(20, 0), padx=10, ipady=7, sticky="ew")
password_label.grid(row=2, column=0, pady=(20, 0))
password_entry.grid(row=2, column=1, pady=(20, 0), padx=10, ipady=7, sticky="ew")
signup_button.grid(row=4, column=0, columnspan=2, pady=20)
show_password_check.grid(row=3, column=0, columnspan=2, pady=10)

# Bind the sign_up function to the Enter key
window.bind('<Return>', sign_up)

window.mainloop()
