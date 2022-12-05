# 学生信息管理系统
card_list = []  # 存放学生信息的列表
headline = []


def load_info():
    """从文件导入学生信息"""
    fr = open("student.txt", 'r',encoding='utf-8')
    head = fr.readline()
    headline.append(head)  # 为后面写入表头做准备
    fr.seek(0, 0)
    lines = fr.readlines()
    field = lines.pop(0).split(',')  # 移除表头
    for eachline in lines:
        t = eachline.split('\t')  # 取出每行数据，即列表 lines 中的一个元素
        t[7] = t[7].strip('\n')  # 删除每行后的换行符
        card_dict = {
            'num_str': t[0],
            'name_str': t[1],
            'class_str': t[2],
            'sex_str': t[3],
            'age_str': t[4],
            'phone_str': t[5],
            'qq_str': t[6],
            'addr_str': t[7]}
        card_list.append(card_dict)  # 将学生信息字典添加到列表中
    print('学生信息成功导入！')
    fr.close()


def save_info():
    fw = open("student.txt", 'w',encoding='utf-8')
    fw.write(" ".join(headline))  # 写入表头
    for i in range(len(card_list)):
        fw.write(card_list[i]["num_str"] + "\t")  # 写入每行有效数据
        fw.write(card_list[i]["name_str"] + "\t")
        fw.write(card_list[i]["class_str"] + "\t")
        fw.write(card_list[i]["sex_str"] + "\t")
        fw.write(card_list[i]["age_str"] + "\t")
        fw.write(card_list[i]["phone_str"] + "\t")
        fw.write(card_list[i]["qq_str"] + "\t")
        fw.write(card_list[i]["addr_str"] + "\n")
    print('学生信息成功保存！')
    fw.close()


def show_menu():
    """显示菜单"""
    print()
    print('*' * 70)
    print('欢迎使用【学生信息管理系统】')
    print()
    print('1.浏览全部')
    print('2.新增学生')
    print('3.搜索学生')
    print('4.修改学生')
    print('5.删除学生')
    print('6.保存信息')
    print('0.退出系统')
    print('*' * 70)
    print()


def new_student():
    """新增学生"""
    print('-' * 70)
    print('新增学生')
    # 提示用户输入学生的详细信息
    num_str = input('请输入学号：')
    name_str = input('请输入姓名：')
    class_str = input('请输入班级：')
    sex_str = input('请输入性别：')
    age_str = input('请输入年龄：')
    phone_str = input('请输入电话：')
    qq_str = input('请输入 QQ：')
    addr_str = input('请输入地址：')
    # 使用用户输入的信息建立一个学生信息字典
    card_dict = {'num_str': num_str,
                 'name_str': name_str,
                 'class_str': class_str,
                 'sex_str': sex_str,
                 'age_str': age_str,
                 'phone_str': phone_str,
                 'qq_str': qq_str,
                 'addr_str': addr_str}
    # 将学生信息字典添加到列表中
    card_list.append(card_dict)  # 一个字典的键值对为列表中的一个元素
    # 提示用户添加成功
    print('添加%s 的信息成功' % name_str)


def show_all():
    """显示所有学生信息"""
    print('-' * 70)
    print('显示所有学生信息')
    # 判断是否存在学生信息记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print('当前没有任何学生记录，请使用新增功能添加学生信息')
        return
    # 打印表头
    for name in ["学号", "姓名", "班级", "性别", "年龄", "   电话", "   QQ", "   地址"]:
        print(name, "\t", end="")
    print('')
    # 打印分隔线
    print('=' * 70)
    # 遍历学生信息列表依次输出字典信息
    for card_dict in card_list:
        print('%-6s\t%-6s\t%-6s\t%-3s\t%-6s\t%-11s\t%-11s\t%6s' % (card_dict['num_str'],
                                                  card_dict['name_str'],
                                                  card_dict['class_str'],
                                                  card_dict['sex_str'],
                                                  card_dict['age_str'],
                                                  card_dict['phone_str'],
                                                  card_dict['qq_str'],
                                                  card_dict['addr_str']))


def search_student():
    """搜索学生信息"""
    print('-' * 70)
    print('搜索学生信息')
    # 1.提示用户输入要搜索的姓名
    find_name = input('请输入要搜索的姓名：')
    # 2.遍历学生信息列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for i in range(len(card_list)):
        if find_name == card_list[i]['name_str']:
            print("学号\t 姓名\t 班级\t 性别\t 年龄\t 电话\tQQ\t 地址")
            print('=' * 70)
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (card_list[i]['num_str'],
                                              card_list[i]['name_str'],
                                              card_list[i]['class_str'],
                                              card_list[i]['sex_str'],
                                              card_list[i]['age_str'],
                                              card_list[i]['phone_str'],
                                              card_list[i]['qq_str'],
                                              card_list[i]['addr_str']))
            break
        else:
            print('抱歉，没有找到%s' % find_name)


def update_student():
    """修改学生信息"""
    find_num = input('请输入待修改学生学号：')
    for i in range(len(card_list)):
        if find_num == card_list[i]['num_str']:
            print("学号\t 姓名\t 班级\t 性别\t 年龄\t 电话\tQQ\t    地址")
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (card_list[i]['num_str'],
                                                card_list[i]['name_str'],
                                                card_list[i]['class_str'],
                                                card_list[i]['sex_str'],
                                                card_list[i]['age_str'],
                                                card_list[i]['phone_str'],
                                                card_list[i]['qq_str'],
                                                card_list[i]['addr_str']))
         # 替换已经存在的键值对(学号不能修改)
            card_list[i]['name_str'] = input_info(card_list[i]['name_str'], '姓名：')
            card_list[i]['class_str'] = input_info(card_list[i]['class_str'], '班级：')
            card_list[i]['sex_str'] = input_info(card_list[i]['sex_str'], '性别：')
            card_list[i]['age_str'] = input_info(card_list[i]['age_str'], '年龄：')
            card_list[i]['phone_str'] = input_info(card_list[i]['phone_str'], '电话：')
            card_list[i]['qq_str'] = input_info(card_list[i]['qq_str'], 'QQ：')
            card_list[i]['addr_str'] = input_info(card_list[i]['addr_str'], '地址：')
            print('修改学生信息成功！！！')
            break
        else:
            print('抱歉，没有找到学号为%s 的学生' % find_num)


def input_info(dict_value, tip_message):
    """
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，负责返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回‘字典中原有的值’
    else:
        return dict_value


def delete_student():
    """删除学生信息"""
    find_num = input('请输入待删除学生学号：')
    for i in range(len(card_list)):
        if find_num == card_list[i]['num_str']:
            del card_list[i]
            break
    print('删除学生信息成功！')