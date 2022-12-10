import tkinter as tk
from tkinter import ttk


class Test:
    def __init__(self, w1):
        self.w1 = w1
        self.w1.configure(bg='powderblue')
        self.columns = ['编号', '语文', '英语']
        # 更改Treeview里面字体大小
        style = ttk.Style()
        style.theme_use("clam")  # 样式
        style.configure("Treeview.Heading", font=('宋体', 12))  # 字体大小
        xbar = ttk.Scrollbar(self.w1, orient='horizontal')  # 水平滚动条
        ybar = ttk.Scrollbar(self.w1, orient='vertical')  # 垂直滚动条
        self.tree = ttk.Treeview(
            self.w1,  #
            height=8,  # 高度
            columns=self.columns,  # 显示的列
            show='headings',  # 隐藏首列
            yscrollcommand=ybar.set,
            xscrollcommand=xbar.set

        )
        ybar['command'] = self.tree.yview
        xbar['command'] = self.tree.xview
        for x in self.columns:
            self.tree.heading(x, text=x)
            self.tree.column(x, width=120, anchor=tk.CENTER)  # 居中对齐
        self.tree.grid(row=0, column=0, columnspan=2)  # columnspan=2合并单元格，横跨2列
        xbar.grid(row=1, column=0, columnspan=2, sticky='we')  # 左右对齐
        ybar.grid(row=0, column=2, sticky='ns')  # 上下对齐

        # 添加按钮
        self.bb1 = tk.Button(self.w1, text='确定', font=('华文行楷', 12), bg='linen', width=12, height=2)
        self.bb1.grid(row=2, column=0, pady=5)
        self.bb2 = tk.Button(self.w1, text='退出', font=('华文行楷', 12), bg='linen', width=12, height=2,
                             command=self.w1.destroy)
        self.bb2.grid(row=2, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('test')
    root.resizable(0, 0)  # 设置窗口不可变
    root.geometry('500x300+100+100')
    Test(root)
    root.mainloop()
