import tkinter
import tkinter as tk
from tkinter.messagebox import *
from WorkTwo.POJO import Stu
from WorkTwo.data import *


def check(id):
    student = []
    student = dao.selectOne(id)
    return student


class Update():
    def __init__(self, root, page):

        root.title('修改')
        root.geometry("500x200+500+300")  # 窗口大小
        self.setup_UI(root, page)

    def setup_UI(self, root, page):

        page.destroy()
        page = tk.Frame(root)
        page.pack()
        tk.Label(page, text='请输入要查询的id号: ', font=20, width=20, pady=15).grid(row=1, column=1)
        self.id = tk.StringVar()
        self.entid = tk.Entry(page, textvariable=self.id, font=(",''20',"), width=25)
        self.id.set("1")
        self.entid.grid(row=1, column=2)
        self.status = tk.StringVar()
        self.statusLabel = tk.Label(page, text='', font=15, fg='red', textvariable=self.status, width=10)
        self.statusLabel.grid(row=2, column=1, columnspan=2)
        tk.Button(page, text="查询", font=20, width=6, command=lambda: self.ok(root, page)).grid(row=4, column=1,
                                                                                                 pady=10, sticky=tk.N)
        # tk.Button(page, text="返回", font=20, width=6, command=self.cancel).grid(row=4, column=2, pady=10, sticky=tk.N)

    def ok(self, root, page):
        self.login(self.id.get(), root, page)

    def login(self, id, root, page):
        if id:
            validate = check(id)
            if len(validate) != 0:
                self.status.set("查找成功")
                print(validate)
                self.setup_UI2(validate, root, page)
            else:
                self.status.set('学号不存在')
        else:
            self.status.set("请输入id号")

    def setup_UI2(self, student: Stu, root, page):
        page.destroy()
        root.geometry("500x700+500+100")
        stu = Stu()
        page = tk.Frame(root)
        page.pack()
        self.stringval = []
        print(student)
        tk.Label(page, text='更新学生信息 ', font=30, width=10, pady=15, padx=15).grid(row=1, column=1, columnspan=5)
        self.stringval.append(tk.StringVar())
        tk.Label(page, text='学号： ', font=20, width=15, pady=15).grid(row=2, column=1)
        tk.Entry(page, textvariable=self.stringval[0], font=(",''20',"), width=10).grid(row=2, column=2)
        self.stringval[0].set(f'{student[0].StuId}')

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='姓名: ', font=20, width=15, pady=15).grid(row=3, column=1)
        tk.Entry(page, textvariable=self.stringval[1], font=20, width=10).grid(row=3, column=2)
        self.stringval[1].set(student[0].Name)

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='性别: ', font=20, width=15, pady=15).grid(row=4, column=1)
        tk.Entry(page, textvariable=self.stringval[2], font=20, width=10).grid(row=4, column=2)
        self.stringval[2].set(student[0].Sex)

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='班级: ', font=20, width=15, pady=15).grid(row=5, column=1)
        tk.Entry(page, textvariable=self.stringval[3], font=20, width=10).grid(row=5, column=2)
        self.stringval[3].set(student[0].ClassName)

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='数学: ', font=20, width=15, pady=15).grid(row=6, column=1)
        tk.Entry(page, textvariable=self.stringval[4], font=20, width=10).grid(row=6, column=2)
        self.stringval[4].set(student[0].Math)

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='语文: ', font=20, width=15, pady=15).grid(row=7, column=1)
        tk.Entry(page, textvariable=self.stringval[5], font=20, width=10).grid(row=7, column=2)
        self.stringval[5].set(student[0].Chinese)

        self.stringval.append(tk.StringVar())
        tk.Label(page, text='英语: ', font=20, width=15, pady=15).grid(row=8, column=1)
        tk.Entry(page, textvariable=self.stringval[6], font=20, width=10).grid(row=8, column=2)
        self.stringval[6].set(student[0].English)

        tk.Button(page, text="修改", font=20, width=6, command=self.updates).grid(row=9, column=1, pady=10)

    def updates(self):
        stu = Stu()
        stu.StuId = self.stringval[0].get()
        stu.Name = self.stringval[1].get()
        stu.Sex = self.stringval[2].get()
        stu.ClassName = self.stringval[3].get()
        stu.Math = self.stringval[4].get()
        stu.Chinese = self.stringval[5].get()
        stu.English = self.stringval[6].get()
        print(stu)
        dao.update(stu.StuId, stu)
        showinfo("提示框", "保存成功")

    # def returns(self):
    #     self.destroy()
    #     Login()
    #
    # def cancel(self):
    #     self.destroy()
    #     pass
