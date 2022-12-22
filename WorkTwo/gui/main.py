import tkinter as tk
from tkinter import *
from login import *

root = Tk()
page = Frame(root)
loginPage(root, page)
img = Image.open("logo.jpg")
img = img.resize((100,100))
photo = ImageTk.PhotoImage(img)
tk.Label(page,image=photo).grid(row=1, column=1,rowspan=3)

root.mainloop()
