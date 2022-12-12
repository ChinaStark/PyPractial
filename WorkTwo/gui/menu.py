import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

import WorkTwo.gui.selectAll
from WorkTwo.POJO import Stu
from WorkTwo.data.dao import *
from WorkTwo.gui import *
from selectAll import *
from matplotlib import pyplot as plt


def show_menu(root, page, ):
    page.destroy()
    page = Frame(root)
    page.pack()
    root.geometry("600x400+450+200")
    root.title("主菜单")

    # 更新学生需要
    StuID = tk.StringVar()
    Stustatus = tk.StringVar()
    stringval = []
    #

    # 删除学生需要
    DelID = tk.StringVar()
    DelStatus = tk.StringVar()
    DelEnterID = None
    DelstatusLabel = None
    #

    # 查询一个学生需要
    seloneID = tk.StringVar()
    selone_enterID = None
    selone_status = tk.StringVar()
    selone_statuslabel = None
    #

    # 查询所有学生需要

    Label(page, text="主菜单功能", font=25).pack(pady=5)
    Button(page, text="添加学生信息", command=lambda: Stu_Add(root, page), width=25, font=28, foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="更新学生信息", command=lambda: Update(root, page, StuID, Stustatus, stringval), width=25,
           font=28,
           foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="删除学生信息", command=lambda: Del(root, page, DelID, DelStatus, DelEnterID, DelstatusLabel),
           width=25, font=28,
           foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="查询一位学生信息",
           command=lambda: SelOne(root, page, seloneID, selone_enterID, selone_status, selone_statuslabel), width=25,
           font=28,
           foreground="black", background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)
    Button(page, text="查询所有学生信息", command=lambda: selectAll(root, page), width=25,
           font=28, foreground="black",
           background="white",
           activebackground="wheat").pack(
        padx=80, pady=3)


# 添加学生模块---add.py
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


# 添加学生模块


# 更新学生模块----update.py
def checkUpdate(id):
    student = []
    student = selectOne(id)
    return student


def Update(root, page, StuID, Stustatus, stringval):
    root.title('修改')
    root.geometry("500x200+500+300")  # 窗口大小
    setup_UpdateUI(root, page, StuID, Stustatus, stringval)


def setup_UpdateUI(root, page, StuID, Stustatus, stringval):
    page.destroy()
    page = Frame(root)
    page.grid()
    tk.Label(page, text='请输入要查询的id号: ', font=20, width=20, pady=15).grid(row=1, column=1)
    # StuID.set("0")
    entid = tk.Entry(page, textvariable=StuID, font=(",''20',"), width=25).grid(row=1, column=2)
    statusLabel = tk.Label(page, font=15, fg='red', textvariable=Stustatus, width=10).grid(row=2,
                                                                                           column=1,
                                                                                           columnspan=2)

    tk.Button(page, text="查询", font=20, width=6,
              command=lambda: Query(StuID.get(), Stustatus, stringval, root, page)).grid(
        row=4,
        column=1,
        pady=10,
        sticky=tk.N)
    tk.Button(page, text="返回", font=20, width=6, command=lambda: show_menu(root, page)).grid(
        row=4,
        column=2,
        pady=10,
        sticky=tk.N)


def Query(StuID, Stustatus, stringval, root, page, ):
    print(StuID)
    if StuID:
        validate = checkUpdate(StuID)
        print(validate)
        if len(validate) != 0:
            Stustatus.set("查找成功")
            print(validate)
            setup_DelUI2(validate, root, page, stringval)
        else:
            print("StuID = ", StuID)
            Stustatus.set('学号不存在')
    else:
        Stustatus.set("请输入id号")


def setup_DelUI2(student: Stu, root, page, stringval: list):
    page.destroy()
    root.geometry("500x700+500+100")
    stu = Stu()
    page = Frame(root)
    page.pack()
    stringval = []
    print(student)
    tk.Label(page, text='更新学生信息 ', font=30, width=10, pady=15, padx=15).grid(row=1, column=1, columnspan=5)
    stringval.append(tk.StringVar())
    tk.Label(page, text='学号： ', font=20, width=15, pady=15).grid(row=2, column=1)
    tk.Entry(page, textvariable=stringval[0], font=(",''20',"), width=10).grid(row=2, column=2)
    stringval[0].set(f'{student[0].StuId}')

    stringval.append(tk.StringVar())
    tk.Label(page, text='姓名: ', font=20, width=15, pady=15).grid(row=3, column=1)
    tk.Entry(page, textvariable=stringval[1], font=20, width=10).grid(row=3, column=2)
    stringval[1].set(student[0].Name)

    stringval.append(tk.StringVar())
    tk.Label(page, text='性别: ', font=20, width=15, pady=15).grid(row=4, column=1)
    tk.Entry(page, textvariable=stringval[2], font=20, width=10).grid(row=4, column=2)
    stringval[2].set(student[0].Sex)

    stringval.append(tk.StringVar())
    tk.Label(page, text='班级: ', font=20, width=15, pady=15).grid(row=5, column=1)
    tk.Entry(page, textvariable=stringval[3], font=20, width=10).grid(row=5, column=2)
    stringval[3].set(student[0].ClassName)

    stringval.append(tk.StringVar())
    tk.Label(page, text='数学: ', font=20, width=15, pady=15).grid(row=6, column=1)
    tk.Entry(page, textvariable=stringval[4], font=20, width=10).grid(row=6, column=2)
    stringval[4].set(student[0].Math)

    stringval.append(tk.StringVar())
    tk.Label(page, text='语文: ', font=20, width=15, pady=15).grid(row=7, column=1)
    tk.Entry(page, textvariable=stringval[5], font=20, width=10).grid(row=7, column=2)
    stringval[5].set(student[0].Chinese)

    stringval.append(tk.StringVar())
    tk.Label(page, text='英语: ', font=20, width=15, pady=15).grid(row=8, column=1)
    tk.Entry(page, textvariable=stringval[6], font=20, width=10).grid(row=8, column=2)
    stringval[6].set(student[0].English)

    tk.Button(page, text="修改", font=20, width=6, command=lambda: updates(stringval)).grid(row=9, column=1, pady=10)
    tk.Button(page, text="返回", font=20, width=6, command=lambda: show_menu(root, page)).grid(row=9, column=22,
                                                                                               pady=10)


def updates(stringval: list):
    stu = Stu()
    stu.StuId = stringval[0].get()
    stu.Name = stringval[1].get()
    stu.Sex = stringval[2].get()
    stu.ClassName = stringval[3].get()
    stu.Math = stringval[4].get()
    stu.Chinese = stringval[5].get()
    stu.English = stringval[6].get()
    print(stu)
    dao.update(stu.StuId, stu)
    showinfo("提示框", "保存成功")


# 更新学生模块


# 删除学生模块---delete.py
def checkDel(id):
    if delete(id):
        return True
    return False


def Del(root, page, DelID, DelStatus, DelEnterID, DelstatusLabel):
    root.title('删除')
    root.geometry("500x200+500+300")  # 窗口大小
    setup_DelUI(root, page, DelID, DelStatus, DelEnterID, DelstatusLabel)


def setup_DelUI(root, page, DelID, DelStatus, DelEnterID, DelstatusLabel):
    page.destroy()
    page = Frame(root)
    page.pack()
    tk.Label(page, text='请输入要删除的id号', font=10, width=20, pady=10).pack(side=tk.TOP)
    DelEnterID = tk.Entry(page, textvariable=DelID, width=15, font=",'font=10',")
    DelEnterID.pack(side=tk.TOP)
    DelstatusLabel = tk.Label(page, text='', fg='red', textvariable=DelStatus, width=36)
    DelstatusLabel.pack(side=tk.TOP)
    tk.Button(page, text="删除", font=8, width=10, command=lambda: fetchDel(DelID, DelStatus)).pack(side=tk.TOP,
                                                                                                    ipadx=2)
    tk.Button(page, text="返回", font=8, width=10, command=lambda: show_menu(root, page)).pack(side=tk.TOP, ipadx=2)


def fetchDel(DelID, DelStatus):
    ans = messagebox.askokcancel('Verify delete', "确定删除?")
    if ans:
        Delok(DelID, DelStatus)


def Delok(DelID, DelStatus):
    DelRes(DelID.get(), DelStatus)


def DelRes(DelID, DelStatus):
    if id:
        validate = checkDel(DelID)
        if validate:
            DelStatus.set("删除成功")
        else:
            DelStatus.set('学号不存在')
    else:
        DelStatus.set("请输入id号")


# 删除学生模块


# 查询一位学生信息---selone.py
def SelOnecheck(id):
    student = []
    student = selectOne(id)
    return student


def SelOne(root, page, seloneID, selone_enterID, selone_status, selone_statuslabel):
    root.title('查询窗口')
    root.geometry("500x150+500+300")  # 窗口大小
    setup_SelOneUI(root, page, seloneID, selone_enterID, selone_status, selone_statuslabel)


def setup_SelOneUI(root, page, seloneID, selone_enterID, selone_status, selone_statuslabel):
    page.destroy()
    page = Frame(root)
    page.pack()
    tk.Label(page, text='请输入要查询的id号: ', font=20, width=20, pady=15).grid(row=1, column=1)
    selenterID = tk.Entry(page, textvariable=seloneID, width=25)
    selenterID.grid(row=1, column=2)
    statusLabel = tk.Label(page, text='', font=15, fg='red', textvariable=selone_status, width=10)
    statusLabel.grid(row=2, column=1, columnspan=2)
    tk.Button(page, text="查询", font=20, width=6, command=lambda: Selone_ok(root, page, seloneID, selone_status)).grid(
        row=4,
        column=1,
        pady=10,
        sticky=tk.N)
    tk.Button(page, text="返回", font=20, width=6, command=lambda: show_menu(root, page)).grid(row=4, column=2,
                                                                                               pady=10,
                                                                                               sticky=tk.N)


def Selone_ok(root, page, seloneID, selone_status):
    Selone_Res(seloneID.get(), root, page, selone_status)


def Selone_Res(seloneID, root, page, selone_status):
    if seloneID:
        validate = SelOnecheck(seloneID)
        if len(validate) != 0:
            selone_status.set("查找成功")
            print(validate)
            Selone_setup_UI2(validate[0], root, page)
        else:
            selone_status.set('学号不存在')
            Selone_setup_UI3(root)
    else:
        self.status.set("请输入id号")


def Selone_setup_UI3(root):
    root.geometry("500x150+500+300")


def Selone_setup_UI2(student: Stu, root, page):
    root.geometry("500x600+500+100")
    tk.Label(page, text='显示学生信息 ', font=30, width=10, pady=15, padx=15).grid(row=5, column=1,
                                                                                   columnspan=5)
    tk.Label(page, text='学号： ', font=20, width=15, pady=15).grid(row=6, column=1)
    tk.Label(page, text=f'{student.StuId}', font=20, width=10, pady=15).grid(row=6, column=2)
    tk.Label(page, text='姓名: ', font=20, width=15, pady=15).grid(row=7, column=1)
    tk.Label(page, text=f'{student.Name}', font=20, width=10, pady=15).grid(row=7, column=2)
    tk.Label(page, text='性别: ', font=20, width=15, pady=15).grid(row=8, column=1)
    tk.Label(page, text=f'{student.Sex}', font=20, width=10, pady=15).grid(row=8, column=2)
    tk.Label(page, text='班级: ', font=20, width=15, pady=15).grid(row=9, column=1)
    tk.Label(page, text=f'{student.ClassName}', font=20, width=10, pady=15).grid(row=9, column=2)
    tk.Label(page, text='数学: ', font=20, width=15, pady=15).grid(row=10, column=1)
    tk.Label(page, text=f'{student.Math}', font=20, width=10, pady=15).grid(row=10, column=2)
    tk.Label(page, text='语文: ', font=20, width=15, pady=15).grid(row=11, column=1)
    tk.Label(page, text=f'{student.Chinese}', font=20, width=10, pady=15).grid(row=11, column=2)
    tk.Label(page, text='英语: ', font=20, width=15, pady=15).grid(row=12, column=1)
    tk.Label(page, text=f'{student.English}', font=20, width=10, pady=15).grid(row=12, column=2)

# 查询一位学生信息
