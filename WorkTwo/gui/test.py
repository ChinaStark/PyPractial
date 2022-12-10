# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# # 选择字体中文显示
plt.rcParams['font.family'] = ['Microsoft YaHei']
# 创建数据
y = [17, 28, 25, 30]
labels = ['A', 'B', 'C', 'D']
colors = ["#d5610d", "#5d9ca9", "#65a509", "#a498c6"]
# 第一个饼状图添加起始角度和阴影并分离
plt.subplot(1, 2, 1)
# 传入数据
plt.pie(y, labels=labels, colors=colors, autopct='%.1f%%', startangle=90, shadow=True, explode=(0, 0.2, 0, 0))
plt.title("加阴影并分离")  # 设置标题
# 第二个饼状图更改标题颜色和文字大小
plt.subplot(1, 2, 2)
# 传入数据
plt.pie(y, labels=labels, colors=colors, autopct='%.1f%%', startangle=90, shadow=True, explode=(0, 0.2, 0, 0))
plt.title("更改标题颜色和10号文字大小", color='purple', fontsize=10)  # 设置标题
plt.suptitle("饼状图对比", color='yellowgreen', fontsize=20)  # 设置总标题
# 绘图
plt.show()
