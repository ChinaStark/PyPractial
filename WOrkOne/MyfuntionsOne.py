card_list = []  # 存放学生信息的列表
headline = []


def load_info():
    """从文件导入学生信息"""
    fr = open("student.txt", 'r')
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
    pass


def show_menu():
    fw = open("student.txt", 'w')
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
    print("学生信息保存成功！")
    fw.close()
    pass


def new_student():

    pass


def search_student():

    pass


def update_student():
    pass


def delete_student():
    pass


def save_info():
    pass


def show_all():
    print('-' * 70)
    print('显示所有学生信息')
    # 判断是否存在学生信息记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print('当前没有任何学生记录，请使用新增功能添加学生信息')
    return
    # 打印表头
    for name in ["学号", "姓名", "班级", "性别", "年龄", "电话", "QQ", "地址"]:
        print(name, "\t", end="")
    print('')
    # 打印分隔线
    print('=' * 70)
    # 遍历学生信息列表依次输出字典信息
    for card_dict in card_list:
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (card_dict['num_str'],
                                                  card_dict['name_str'],
                                                  card_dict['class_str'],
                                                  card_dict['sex_str'],
                                                  card_dict['age_str'],
                                                  card_dict['phone_str'],
                                                  card_dict['qq_str'],
                                                  card_dict['addr_str']))
    pass
