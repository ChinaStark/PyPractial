import tkinter as tk
from tkinter.messagebox import *
from WorkTwo.data import *
from menu import show_menu


def check(id):
    if dao.delete(id):
        return True
    return False


def delete(root,page):

    root.title('删除')
    root.geometry("500x200+500+300")  #窗口大小
    setup_UI(root,page)

def setup_UI(root,page):
    page.pack()
    tk.Label(page,text='请输入要删除的id号',font=10,width=20,pady=10).pack(side=tk.TOP)
    ids = tk.StringVar()

    entrys = tk.Entry(page, textvariable=ids,font=(",''20',"),width=15)
    entrys.pack(side=tk.TOP)
    global status
    status=tk.StringVar()
    statusLabel = tk.Label(page,text='',fg='red',textvariable=status,width=36)
    statusLabel.pack(side=tk.TOP)
    tk.Button(page,text="删除",font=8,width=10,command=lambda :fetch(ids)).pack(side=tk.TOP,ipadx=2)
    tk.Button(page,text="返回",font=8,width=10,command=cancel(root)).pack(side=tk.TOP,ipadx=2)
    page.mainloop()

def fetch(ids):
    id = ids.get()
    ans = askokcancel('Verify delete', "确定删除?")
    if ans:
        login( id)

def login(id):

    if id :
        validate = check(id)
        if validate:
            status.set("删除成功")
        else:
            status.set('学号不存在')
    else:
        status.set("请输入id号")


def cancel(root):
    root.destroy()
    show_menu()

def dels():
    root = tk.Tk()
    page = tk.Frame(root)
    delete(root,page)