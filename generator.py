# Import libraries
import tkinter as tk
from tkinter import ttk
import random
import pyperclip
import string
from PIL import Image, ImageTk

# Window
window = tk.Tk()
window.geometry('384x256')
window.resizable(False, False)
window.config(bg = 'pink')
window.title('Password Generator')

# Labels
info_label = ttk.Label(
    text = 'Random Password Generator',
     font = 'verdana 15 bold', 
     foreground = 'white', 
     background = 'black').place(relx = .5, y = 50, anchor = tk.CENTER)

length_label = ttk.Label(
    text = 'Password length:', 
    font = 'verdana 10 bold', 
    foreground = 'black', 
    background = 'pink').place(relx = .33, y = 100, anchor = tk.CENTER)

# Spinbox
length_spinbox = ttk.Spinbox(from_ = 1, to = 32)
length_spinbox.place(relx = .7, y = 100, anchor = tk.CENTER)

# Text widget
display = tk.Text(width = 32, height = 1, state = 'disabled')
display.place(relx = .5, y = 175, anchor = tk.CENTER)

# Functions
def generate():
    characters = string.ascii_letters + string.digits + string.punctuation
    length = int(length_spinbox.get())
    password = ''.join(random.choices(characters, k = length))
    display.configure(state = 'normal')
    display.delete(1.0, tk.END)
    display.insert(1.0, password)
    display.configure(state = 'disabled')

def copy():
    pyperclip.copy(display.get(1.0, tk.END))

# Buttons
generate_button = ttk.Button(text = 'Generate!', command = generate)
generate_button.place(relx = .5, y = 150, anchor = tk.CENTER)
img = Image.open('copy.png').resize([20, 20])
image = ImageTk.PhotoImage(img)
copy_button = ttk.Button(image = image, command = copy)
copy_button.place(x = 350, y = 175, anchor = tk.CENTER)


window.mainloop()
