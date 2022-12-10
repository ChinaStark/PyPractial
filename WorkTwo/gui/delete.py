import tkinter as tk
from tkinter.messagebox import *
from WorkTwo.data import *


def check(id):
    if dao.delete(id):
        return True
    return False


class Del():
    def __init__(self, root, page):
        root.title('删除')
        root.geometry("500x200+500+300")  # 窗口大小
        self.setup_UI(root, page)

    def setup_UI(self, root, page):
        page.destroy()
        page = tk.Frame(root)
        page.pack()
        tk.Label(page, text='请输入要删除的id号', font=10, width=20, pady=10).pack(side=tk.TOP)
        self.id = tk.StringVar()
        self.entid = tk.Entry(page, textvariable=self.id, width=15, font=",'font=10',")
        self.entid.pack(side=tk.TOP)
        self.status = tk.StringVar()
        self.statusLabel = tk.Label(page, text='', fg='red', textvariable=self.status, width=36)
        self.statusLabel.pack(side=tk.TOP)
        tk.Button(page, text="删除", font=8, width=10, command=self.fetch).pack(side=tk.TOP, ipadx=2)
        # tk.Button(page, text="返回", font=8, width=10, command=self.cancel).pack(side=tk.TOP, ipadx=2)

    def fetch(self):
        ans = askokcancel('Verify delete', "确定删除?")
        if ans:
            self.ok()

    def ok(self):
        self.login(self.id.get())

    def login(self, id):
        if id:
            validate = check(id)
            if validate:
                self.status.set("删除成功")
            else:
                self.status.set('学号不存在')
        else:
            self.status.set("请输入id号")

    # def cancel(self):
    #     self.destroy()
    #     pass

# def DelPage(root, page):
#     Del(root, page)
