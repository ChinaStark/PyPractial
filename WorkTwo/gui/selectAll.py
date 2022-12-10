from tkinter import ttk
from tkinter import *
from WorkTwo.POJO import Stu
import WorkTwo.data.dao
from WorkTwo.data.dao import *
from matplotlib import pyplot as plt


def fun():
    stulist = WorkTwo.data.dao.selectAll()
    Mathcount = []
    engcount = []
    chinese = []
    ma, mb, mc, md, me = 0, 0, 0, 0, 0
    ea, eb, ec, ed, ee = 0, 0, 0, 0, 0
    ca, cb, cc, cd, ce = 0, 0, 0, 0, 0
    # Create three subplots sharing x axis
    for index, Stu in enumerate(stulist):  # 写入数据
        Mathcount.append(int(Stu.Math))
        engcount.append(int(Stu.English))
        chinese.append(int(Stu.Chinese))
    for i in range(len(Mathcount)):
        if Mathcount[i] < 60:
            me += 1
        elif 60 <= Mathcount[i] < 70:
            md += 1
        elif 70 <= Mathcount[i] < 80:
            mc += 1
        elif 80 <= Mathcount[i] < 90:
            mb += 1
        else:
            ma += 1
    for i in range(len(engcount)):
        if engcount[i] < 60:
            ee += 1
        elif 60 <= engcount[i] < 70:
            ed += 1
        elif 70 <= engcount[i] < 80:
            ec += 1
        elif 80 <= engcount[i] < 90:
            eb += 1
        else:
            ea += 1
    for i in range(len(chinese)):
        if chinese[i] < 60:
            ce += 1
        elif 60 <= chinese[i] < 70:
            cd += 1
        elif 70 <= chinese[i] < 80:
            cc += 1
        elif 80 <= chinese[i] < 90:
            cb += 1
        else:
            ca += 1







    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)  # sharex=False, sharey=False

    plt.rcParams['font.sans-serif'] = ['SimHei']
    labels = ['优', '良', '中', '合格', '差']  # 定义各个扇形的面积/标签
    SizeMath = [ma, mb, mc, md, me]  # 各个值，影响各个扇形的面积
    Sizechinese = [ca, cb, cc, cd, ce]
    SizeEnglish = [ea, eb, ec, ed, ee]
    colors = ['red', 'yellowgreen', 'lightskyblue', 'yellow', 'purple']  # 每块扇形的颜色
    explode = (0.01, 0.01, 0.01, 0.01, 0.01)
    ax1.pie(SizeMath, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1
            )  # 数值距圆心半径倍数距离
    plt.subplot(1, 3, 1)
    plt.title("语文成绩统计")
    ax2.pie(SizeMath, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1)  # 数值距圆心半径倍数距离
    plt.subplot(1, 3, 2)
    plt.title("数学成绩统计")
    ax3.pie(SizeMath, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1)  # 数值距圆心半径倍数距离
    plt.subplot(1, 3, 3)
    plt.title("语文成绩统计")
    plt.show()


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
treeview.grid(row=0, column=0)
# treeview.pack(side=TOP)
stulist = WorkTwo.data.dao.selectAll()
Button(text='成绩概览', height=2, width=13, bg="gray", command=fun).grid(row=1, column=0, padx=10, pady=10)

for index, Stu in enumerate(stulist):  # 写入数据
    treeview.insert('', index, values=(Stu.StuId, Stu.Name, Stu.ClassName, Stu.Sex, Stu.Math, Stu.Chinese, Stu.English))
root.mainloop()  # 进入消息循环
