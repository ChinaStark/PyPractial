import tkinter
import tkinter as tk
from tkinter.messagebox import *

from WorkTwo.POJO import Stu
from WorkTwo.data import *
def check(id) :
    student = []
    student = dao.selectOne(id)
    return student





def selectone(root, page):
    root.title('Login')
    root.geometry("500x150+500+300")  # 窗口大小
    setup_UI(root, page)


def setup_UI(root, page):
    page.pack()
    tk.Label(page,text='请输入要查询的id号: ',font=20,width=20,pady=15).grid(row=1,column=1)
    id = tk.StringVar()
    entid = tk.Entry(page,textvariable=id,width=25)
    entid.grid(row=1,column=2)
    global status
    status=tk.StringVar()
    statusLabel = tk.Label(page,text='',font=15,fg='red',textvariable=status,width=10)
    statusLabel.grid(row=2,column=1,columnspan=2)
    tk.Button(page,text="返回",font=20,width=6,command=cancel).grid(row=4,column=2,pady=10,sticky=tk.N)
    tk.Button(page, text="查询",font=20, width=6, command=lambda :ok(id,root,page)).grid(row=4,column=1,pady=10,sticky=tk.N)
    page.mainloop()


def ok(id,root,page):
    login(id.get(),root,page)
def login(id,root,page):
    if id :
        validate = check(id)
        if len(validate) != 0:
            status.set("查找成功")
            print(validate)
            setup_UI2(validate[0],root,page)
        else:
            status.set('学号不存在')
            setup_UI3(root, page )
    else:
        status.set("请输入id号")

def setup_UI3(root, page ) :
    root.geometry("500x150+500+300")


def setup_UI2(student:Stu,root,page) :
    root.geometry("500x600+500+100")
    tk.Label(page, text='学生信息 ',font=30, width=10, pady=15,padx=15).grid(row=5, column=1,columnspan=5)
    tk.Label(page, text='学号： ', font=20,  width=15, pady=15).grid(row=6,column=1)
    tk.Label(page, text=f'{student.StuId}',font=20, width=10, pady=15).grid(row=6,column=2 )
    tk.Label(page, text='姓名: ', font=20,width=15, pady=15).grid(row=7, column=1)
    tk.Label(page, text=f'{student.Name}',font=20, width=10, pady=15).grid(row=7, column=2)
    tk.Label(page, text='性别: ',font=20, width=15, pady=15).grid(row=8, column=1)
    tk.Label(page, text=f'{student.Sex}',font=20, width=10, pady=15).grid(row=8, column=2)
    tk.Label(page, text='班级: ',font=20, width=15, pady=15).grid(row=9, column=1)
    tk.Label(page, text=f'{student.ClassName}', font=20,width=10, pady=15).grid(row=9, column=2)
    tk.Label(page, text='数学: ',font=20, width=15, pady=15).grid(row=10, column=1)
    tk.Label(page, text=f'{student.Math}',font=20, width=10, pady=15).grid(row=10, column=2)
    tk.Label(page, text='语文: ',font=20, width=15, pady=15).grid(row=11, column=1)
    tk.Label(page, text=f'{student.Chinese}', font=20,width=10, pady=15).grid(row=11, column=2)
    tk.Label(page, text='英语: ',font=20, width=15, pady=15).grid(row=12, column=1)
    tk.Label(page, text=f'{student.English}',font=20, width=10, pady=15).grid(row=12, column=2)


def cancel():
    pass

def select():
    root = tk.Tk()
    page = tk.Frame(root)

    selectone(root, page)