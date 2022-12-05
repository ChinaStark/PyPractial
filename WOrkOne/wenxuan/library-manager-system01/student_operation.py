

from Student import Student


class StudentDao:

    card_list:list[Student] = []
    headline = None

    def show_menu(self):
        """
            显示菜单
        """
        pass


    def load_info(self):
        """
        从文件导入学生信息，将文件中的学生信息保存到列表中
        """
        pass

    def save_info(self):
        """
        将列表中的学生信息保存到文件中
        """
        pass

    def new_student(self):
        """
        将学生信息保存到列表中
        :return:
        """
        pass

    def show_all(self):
        """
        将列表中所有信息显示出来
        :return:
        """
        pass

    def search_student(self, name):
        """
        查找姓名为name的学生信息
        :param name: 学生姓名
        :return:
        """
        pass

    def input_info(self, old_value, tip_message:str) -> str:
        """
        提示用户输入对应的值
        :param old_value:  学生原来的信息
        :param tip_message: 提示用户的信息
        :return: 如果用户没有输入信息，则返回原来信息dict_value，如果用户输入了信息就返回用户输入的信息
        """
        pass

    def update_student(self, id:str):
        """
        通过学生id修改学生信息
        :param id: 学生学号
        :return:
        """
        pass



    def delete_student(self, id:str):
        """
        通过学生id删除学生信息
        :param id: 学生学号
        :return:
        """
        pass






class StudentDaoImpl(StudentDao):


    def __init__(self, path):
        self.headline = "学号\t姓名\t班级\t性别\t年龄\t电话\tQQ\t地址"
        self.path = path
        self.load_info()        # 加载文件内容



    def show_menu(self):
        print("*" * 70)
        print("欢迎使用学生管理系统")
        print("1.浏览全部学生信息")
        print("2.新增学生信息")
        print("3.查找学生信息")
        print("4.修改学生信息")
        print("5.删除学生信息")
        print("6.保存学生信息")
        print("0.退出系统")
        print("*" * 70)


    def load_info(self):
        print("*" * 70)
        file = open(self.path, "r", encoding="UTF-8")
        lines = file.readlines()        # 读取整个文件
        lines.pop(0)                    # 移除第一行数据
        for eachline in lines:
            data = eachline.split("\t") # 获取每一行中的每一列数据
            student = Student(data[0], data[1], int(data[2]), data[3], int(data[4]), data[5], data[6], data[7])
            self.card_list.append(student)
        print("学生信息导入成功")
        file.close()

    def save_info(self):
        print("保存学生信息：")
        file = open(self.path, "w", encoding="UTF-8")
        file.write(self.headline)       # 先将文件头写入
        for student in self.card_list:
            file.write(f"{student.id}\t")
            file.write(f"{student.name}\t")
            file.write(f"{student.classed}\t")
            file.write(f"{student.sex}\t")
            file.write(f"{student.phone}\t")
            file.write(f"{student.qq}\t")
            file.write(f"{student.address}\t")
        print("学生信息保存成功")
        file.close()


    def new_student(self):
        print("新增学生:")
        id = input("请输入学生学号：")
        name = input("请输入学生姓名：")
        classed = int(input("请输入学生班级："))
        sex = input("请输入学生性别：")
        age = int(input("请输入学生年龄："))
        phone = input("请输入学生电话：")
        qq = input("请输入学生QQ：")
        address = input("请输入学生地址：")
        student = Student(id, name, classed, sex, age, phone, qq, address)
        self.card_list.append(student)
        print(f"成功新增{name}学生")
        print("*" * 70)

    def show_all(self):
        print()
        print("*" * 70)
        print("显示所有学生信息：")
        if(len(self.card_list) == 0):
            print("当前没有学生记录，请使用新增功能添加学生信息")
            return
        print(self.headline)        # 打印表头
        for student in self.card_list:
            print(f"{student.id}\t", end='')
            print(f"{student.name}\t", end='')
            print(f"{student.classed}\t", end='')
            print(f"{student.sex}\t", end='')
            print(f"{student.age}\t", end='')
            print(f"{student.phone}\t", end='')
            print(f"{student.qq}\t", end='')
            print(f"{student.address}\t", end='')
            print()
        print("*" * 70)


    def search_student(self, name):
        print("搜索学生信息")
        for student in self.card_list:
            if name == student.name:
                print(self.headline)    # 打印表头
                print(f"{student.id}\t", end='')
                print(f"{student.name}\t", end='')
                print(f"{student.classed}\t", end='')
                print(f"{student.sex}\t", end='')
                print(f"{student.age}\t", end='')
                print(f"{student.phone}\t", end='')
                print(f"{student.qq}\t", end='')
                print(f"{student.address}\t", end='')
                print()
                return
        print(f"抱歉，没有找到{name}")
        print("*" * 70)


    def input_info(self, old_value, tip_message):
        result = input(tip_message)
        if len(result) > 0:
            return result
        else:
            return old_value

    def update_student(self, id:str):
        print("修改学生信息")
        for s in self.card_list:
            if id == s.id:
                s.name = self.input_info(s.name, "姓名：")
                s.classed = self.input_info(s.classed, "班级：")
                s.sex = self.input_info(s.sex, "性别：")
                s.age = int(self.input_info(s.age, "年龄："))
                s.phone = self.input_info(s.phone, "电话：")
                s.qq = self.input_info(s.qq, "QQ：")
                s.address = self.input_info(s.address, "地址：")
                print(f"学号为{id}的学生信息修改成功")
                return
        print(f"抱歉，不存在学号为{id}的学生")
        print("*" * 70)


    def delete_student(self, id:str):

        for student in self.card_list:
            if id == student.id:
                self.card_list.remove(student)
                print(f"成功删除学号为{id}的学生信息")
                return
        print(f"不存在学号为{id}的学生信息")






