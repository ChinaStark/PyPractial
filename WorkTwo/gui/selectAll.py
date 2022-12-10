from tkinter import ttk
from tkinter import *

import WorkTwo.data.dao
from WorkTwo.data.dao import *

root = Tk()  # 初始框的声明
root.geometry('700x300+100+100')

columns = ("学号", "姓名", "班级", "性别", "语文", "数学", "英语")
treeview = ttk.Treeview(root, height=8, show="headings", columns=columns
                        )  # 表格

ybar = Scrollbar(treeview, orient='vertical', command=treeview.yview)
ybar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)

treeview.config(yscrollcommand=ybar.set)

treeview.column("学号", width=100, anchor='center')  # 表示列,不显示
treeview.column("姓名", width=100, anchor='center')
treeview.column("班级", width=100, anchor='center')
treeview.column("性别", width=100, anchor='center')  # 表示列,不显示
treeview.column("语文", width=100, anchor='center')
treeview.column("数学", width=100, anchor='center')
treeview.column("英语", width=100, anchor='center')

treeview.heading("学号", text="学号")
treeview.heading("姓名", text="姓名")
treeview.heading("班级", text="班级")
treeview.heading("性别", text="性别")
treeview.heading("语文", text="语文")
treeview.heading("数学", text="数学")
treeview.heading("英语", text="英语")
treeview.pack(side=LEFT, anchor=N)

stulist = WorkTwo.data.dao.selectAll()

for index, Stu in enumerate(stulist):  # 写入数据
    treeview.insert('', index, values=(Stu.StuId, Stu.Name, Stu.ClassName, Stu.Sex, Stu.Math, Stu.Chinese, Stu.English))
root.mainloop()  # 进入消息循环
