from tkinter import *
import main


# Main Tkinter window
window = Tk()
window.title("Credits")
window.geometry('500x500')
window.configure(bg='#333333')

# Creating widgets
frame = Frame(window, bg='#333333')
frame.pack(expand=True)

# Widgets
leader = Label(frame, text="Programming by:", bg='#333333', fg="#315257", font=("Arial", 20))
leader.grid(row=2, column=0,  sticky="news", pady=20)
designer = Label(frame, text="Designed by:", bg='#333333', fg="#315257", font=("Arial", 20))
designer.grid(row=3, column=0,  sticky="news", pady=20)
Researcher = Label(frame, text="Research by:", bg='#333333', fg="#315257", font=("Arial", 20))
Researcher.grid(row=4, column=0,  sticky="news", pady=20)
leader = Label(frame, text="Busingye David", bg='#333333', fg="#9fe3e2", font=("Arial", 20))
leader.grid(row=2, column=1,  sticky="news", pady=20)
designer = Label(frame, text="Mulungi Cyrus", bg='#333333', fg="#9fe3e2", font=("Arial", 20))
designer.grid(row=3, column=1,  sticky="news", pady=20)
Researcher = Label(frame, text="Walugembe Gabriel", bg='#333333', fg="#9fe3e2", font=("Arial", 20))
Researcher.grid(row=4, column=1,  sticky="news", pady=20)



window.mainloop()
