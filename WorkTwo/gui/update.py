import tkinter
import tkinter as tk
from tkinter.messagebox import *

from WorkTwo.POJO import Stu
from WorkTwo.data import *
def check(id) :
    student = []
    student = dao.selectOne(id)
    return student





def function(root,page):

    root.title('修改')
    root.geometry("500x200+500+300")  # 窗口大小

    setup_UI(root,page)


def setup_UI(root,page):
    page.pack()
    tk.Label(page, text='请输入要查询的id号: ', font=20, width=20, pady=15).grid(row=1, column=1)
    id = tk.StringVar()
    entid = tk.Entry(page, textvariable=id,font=(",''20',") , width=25)

    entid.grid(row=1, column=2)
    global status
    status = tk.StringVar()
    statusLabel = tk.Label(page, text='', font=15, fg='red', textvariable=status, width=10)
    statusLabel.grid(row=2, column=1, columnspan=2)
    tk.Button(page, text="返回", font=20, width=6, command=lambda :cancel(root)).grid(row=4, column=2, pady=10,sticky=tk.N)
    tk.Button(page, text="查询", font=20, width=6, command=lambda :ok(id,root,page)).grid(row=4, column=1, pady=10, sticky=tk.N)
    page.mainloop()

def ok(id,root,page):
    login(id,root,page)
def login(ids,root,page):
    id = ids.get()
    if id :
        validate = check(id)
        if len(validate) != 0:
            status.set("查找成功")
            print(validate)
            setup_UI2(validate,root,page)
        else:
            status.set('学号不存在')
    else:
        status.set("请输入id号")



def setup_UI2(student,root,page) :
    root.geometry("500x700+500+100")
    stu = Stu()
    page = tk.Frame(root)
    page.pack()
    stringval =[]
    print(student)
    tk.Label(page, text='学生信息 ', font=30, width=10, pady=15, padx=15).grid(row=1, column=1, columnspan=5)
    stringval.append(tk.StringVar())
    tk.Label(page, text='学号： ', font=20, width=15, pady=15).grid(row=2, column=1)
    tk.Entry(page,textvariable=stringval[0], font=(",''20',") ,width=10).grid(row=2, column=2)
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

    tk.Button(page, text="修改", font=20, width=6, command=lambda :updates(stringval,root,page)).grid(row=9, column=1, pady=10)
    tk.Button(page, text="返回", font=20, width=6, command=lambda :returns(root)).grid(row=9, column=2, pady=10)
    page.mainloop()

def updates(stringval,root,page):
    stu = Stu()
    stu.StuId = stringval[0].get()
    stu.Name = stringval[1].get()
    stu.Sex = stringval[2].get()
    stu.ClassName = stringval[3].get()
    stu.Math = stringval[4].get()
    stu.Chinese = stringval[5].get()
    stu.English = stringval[6].get()
    print(stu)
    dao.update(stu.StuId,stu)
    showinfo("提示框","保存成功")
    root.destroy()


def returns(root):
    root.destroy()

def cancel(root):
    root.destroy()
    pass



def up():
    root = tk.Tk()
    page = tk.Frame(root)
    function(root,page)