import tkinter
import tkinter as tk
from tkinter.messagebox import *

from WorkTwo.POJO import Stu
from WorkTwo.data import *
def check(id) :
    student = []
    student = dao.selectOne(id)
    return student



class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry("500x150+500+300")  # 窗口大小
        self.setup_UI()


    def setup_UI(self):

        self.page = tk.Frame(self)
        self.page.pack()
        tk.Label(self.page,text='请输入要查询的id号: ',font=20,width=20,pady=15).grid(row=1,column=1)
        self.id = tk.StringVar()
        self.entid = tk.Entry(self.page,textvariable=self.id,width=25)
        self.entid.grid(row=1,column=2)
        self.status=tk.StringVar()
        self.statusLabel = tk.Label(self.page,text='',font=15,fg='red',textvariable=self.status,width=10)
        self.statusLabel.grid(row=2,column=1,columnspan=2)
        tk.Button(self.page,text="返回",font=20,width=6,command=self.cancel).grid(row=4,column=2,pady=10,sticky=tk.N)
        tk.Button(self.page, text="查询",font=20, width=6, command=self.ok).grid(row=4,column=1,pady=10,sticky=tk.N)

    def ok(self):
        self.login(self.id.get())
    def login(self,id):
        if id :
            validate = check(id)
            if len(validate) != 0:
                self.status.set("查找成功")
                print(validate)
                self.setup_UI2(validate[0])
            else:
                self.status.set('学号不存在')
                self.setup_UI3( )
        else:
            self.status.set("请输入id号")

    def setup_UI3(self ) :
        self.geometry("500x150+500+300")


    def setup_UI2(self,student:Stu) :
        self.geometry("500x600+500+100")
        tk.Label(self.page, text='学生信息 ',font=30, width=10, pady=15,padx=15).grid(row=5, column=1,columnspan=5)
        tk.Label(self.page, text='学号： ', font=20,  width=15, pady=15).grid(row=6,column=1)
        tk.Label(self.page, text=f'{student.StuId}',font=20, width=10, pady=15).grid(row=6,column=2 )
        tk.Label(self.page, text='姓名: ', font=20,width=15, pady=15).grid(row=7, column=1)
        tk.Label(self.page, text=f'{student.Name}',font=20, width=10, pady=15).grid(row=7, column=2)
        tk.Label(self.page, text='性别: ',font=20, width=15, pady=15).grid(row=8, column=1)
        tk.Label(self.page, text=f'{student.Sex}',font=20, width=10, pady=15).grid(row=8, column=2)
        tk.Label(self.page, text='班级: ',font=20, width=15, pady=15).grid(row=9, column=1)
        tk.Label(self.page, text=f'{student.ClassName}', font=20,width=10, pady=15).grid(row=9, column=2)
        tk.Label(self.page, text='数学: ',font=20, width=15, pady=15).grid(row=10, column=1)
        tk.Label(self.page, text=f'{student.Math}',font=20, width=10, pady=15).grid(row=10, column=2)
        tk.Label(self.page, text='语文: ',font=20, width=15, pady=15).grid(row=11, column=1)
        tk.Label(self.page, text=f'{student.Chinese}', font=20,width=10, pady=15).grid(row=11, column=2)
        tk.Label(self.page, text='英语: ',font=20, width=15, pady=15).grid(row=12, column=1)
        tk.Label(self.page, text=f'{student.English}',font=20, width=10, pady=15).grid(row=12, column=2)

    def cancel(self):
        pass

if __name__ == '__main__':
    Login().mainloop()