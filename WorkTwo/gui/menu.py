import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import WorkTwo.gui.selectone
from WorkTwo.POJO import Stu
from WorkTwo.data.dao import *
from WorkTwo.gui.selectAll import *
from update import *
from delete import *
from selectone import *
from matplotlib import pyplot as plt


def show_menu(root, page):
    page.destroy()
    page = Frame(root)
    page.pack()
    root.geometry("600x400+450+200")
    root.title("主菜单")
    Label(page, text="主菜单功能", font=25).pack(pady=5)
    Button(page, text="添加学生信息", command=lambda: Stu_Add(root, page), width=25, font=28, foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="更新学生信息", command=lambda: UpdatePage(root, page), width=25, font=28, foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="删除学生信息", command=lambda: DelPage(root, page), width=25, font=28,
           foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="查询一位学生信息", command=lambda: WorkTwo.gui.selectone.SelOne(root, page), width=25,
           font=28,
           foreground="black", background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="查询所有学生信息", command=lambda: WorkTwo.gui.selectAll.selectAll(root, page), width=25,
           font=28, foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)


def Stu_Add(root, page):
    Stu_ID = tk.StringVar()
    Stu_Classname = tk.StringVar()
    Stu_Name = tk.StringVar()
    Stu_Sex = tk.StringVar()
    Stu_Chinese = tk.StringVar()
    Stu_Math = tk.StringVar()
    Stu_English = tk.StringVar()

    page.destroy()
    page = Frame(root)
    page.pack()
    root.geometry("500x400+300+100")
    root.title("添加学生信息")
    tk.Label(page).grid(row=0, column=0)
    tk.Label(page, text="学生学号：", padx=80, font=20).grid(row=1, column=1)
    tk.Entry(page, textvariable=Stu_ID, font=("", 16, "")).grid(row=1, column=2)
    tk.Label(page, text="学生姓名：", font=20).grid(row=2, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_Name, font=("", 16, "")).grid(row=2, column=2)
    tk.Label(page, text="学生性别：", font=20).grid(row=3, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_Sex, font=("", 16, "")).grid(row=3, column=2)
    tk.Label(page, text="学生班级：", font=20).grid(row=4, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_Classname, font=("", 16, "")).grid(row=4, column=2)
    tk.Label(page, text="数学成绩：", font=20).grid(row=5, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_Math, font=("", 16, "")).grid(row=5, column=2)
    tk.Label(page, text="语文成绩：", font=20).grid(row=6, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_Chinese, font=("", 16, "")).grid(row=6, column=2)
    tk.Label(page, text="英语成绩：", font=20).grid(row=7, column=1, pady=10)
    tk.Entry(page, textvariable=Stu_English, font=("", 16, "")).grid(row=7, column=2)

    tk.Button(page, text="确认",
              command=lambda: addStuInfo(Stu_ID, Stu_Name, Stu_Sex, Stu_Classname, Stu_Math, Stu_Chinese, Stu_English),
              width=10, height=2, font=("", 12, ""),
              activebackground="skyblue").grid(row=8, column=1, pady=10)
    tk.Button(page, text="返回", command=lambda: show_menu(root, page), width=10, height=2, font=("", 12, "")).grid(
        row=8, column=2, padx=5)


def addStuInfo(Stu_ID, Stu_Name, Stu_Sex, Stu_Classname, Stu_Math, Stu_Chinese, Stu_English):
    stu = Stu(Stu_ID.get(), Stu_Name.get(), Stu_Sex.get(), Stu_Classname.get(), Stu_Math.get(), Stu_Chinese.get(),
              Stu_English.get())
    if insert(stu) == True:
        messagebox.showinfo("提示框", "添加成功！")

    else:
        messagebox.showerror("错误", "添加失败！学生的学号不能重复")


def DelPage(root, page):
    Del(root, page)


def UpdatePage(root, page):
    Update(root, page)


def selectOne(root, page):
    SelOne(root, page)
