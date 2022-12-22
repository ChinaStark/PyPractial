import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

import WorkTwo
from WorkTwo.POJO import Stu
from WorkTwo.data import dao
from WorkTwo.data.dao import *
from WorkTwo.gui import *
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
    tk.Label(page, text="学生学号：", padx=10, font=20).grid(row=1, column=1)
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
    root.geometry("500x500+500+100")
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
    ans = messagebox.askokcancel('Verify delete', f"确定删除该的学生吗?")
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
        selone_status.status.set("请输入id号")


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


def Stu_Table():
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
    ax1.pie(SizeEnglish, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1
            )  # 数值距圆心半径倍数距离

    ax2.pie(Sizechinese, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1)  # 数值距圆心半径倍数距离

    ax3.pie(SizeMath, explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=0.5,  # 图例距圆心半径倍距离
            autopct='%3.2f%%',  # 数值保留固定小数位
            shadow=False,  # 无阴影设置
            startangle=90,  # 逆时针起始角度设置
            pctdistance=1.1)  # 数值距圆心半径倍数距离
    plt.subplot(1, 3, 1)
    plt.title("英语成绩统计")
    plt.subplot(1, 3, 2)
    plt.title("语文成绩统计")
    plt.subplot(1, 3, 3)
    plt.title("数学成绩统计")

    # plt.title("成绩图表")
    plt.show()


def selectAll(root, page):
    page.destroy()
    page = Frame(root)
    page.grid()

    root.geometry('700x300+450+150')
    root.title("成绩概览")
    columns = ("学号", "姓名", "班级", "性别", "语文", "数学", "英语")
    treeview = ttk.Treeview(page, height=8, show="headings", columns=columns)  # 表格

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
    treeview.grid(row=0, column=0, columnspan=2)
    stulist = WorkTwo.data.dao.selectAll()
    Button(page, text='成绩概览', height=2, width=13, bg="gray", command=Stu_Table).grid(row=1, column=0, padx=10, pady=10)
    Button(page, text='返回', height=2, width=13, bg="gray", command=lambda: show_menu(root, page)).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)
    m, c, e = 0, 0, 0
    Index = 0
    for index, Stu in enumerate(stulist):  # 写入数据
        Index += 1
        m += int(Stu.Math)
        c += int(Stu.Chinese)
        e += int(Stu.English)
        treeview.insert('', index,
                        values=(Stu.StuId, Stu.Name, Stu.ClassName, Stu.Sex, Stu.Math, Stu.Chinese, Stu.English))

    treeview.insert('', Index + 1, values=(' ', ' ', ' ', '平均分', int(m / Index), int(c / Index), int(e / Index)))
