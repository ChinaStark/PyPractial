import tkinter as tk
from tkinter import *
from menu import show_menu
from tkinter import messagebox
from PIL import Image,ImageTk
from WorkTwo.data.dao import *


def loginPage(root, page):
    username = StringVar()
    password = StringVar()

    root.geometry("350x180+600+300")

    root.title("登录界面")
    page.pack()
    tk.Label(page).grid(row=0, column=5,columnspan=3)
    tk.Label(page, text="用户名：").grid(row=1, column=2)
    tk.Entry(page, textvariable=username, font=("", 10, "")).grid(row=1, column=3)
    tk.Label(page, text="密码：").grid(row=2, column=2, pady=10)
    tk.Entry(page, textvariable=password, show="*", font=("", 10, "")).grid(row=2, column=3)

    loginBtn = tk.Button(page, text="登录", font=25, command=lambda: Check(username, password, root, page))
    loginBtn.grid(row=3, column=2, pady=10, padx=20)
    exitBtn = tk.Button(page, text="退出", font=25, command=page.quit)
    exitBtn.grid(row=3, column=3)


def Check(username, password, root, page):
    user = User(username.get(), password.get())
    # print(user.Username, user.Password)
    if login(user) == True:
        messagebox.showinfo("登录提示", "登录成功")

        page.destroy()
        show_menu(root, page)
    else:
        messagebox.showerror("错误提示", "请检查用户名或密码是否正确")
