from pymysql import Connection

class StudentDao:
    headline = None
    host = "localhost"      # 主机号
    port = 3308             # 端口号
    user = "root"           # 用户名
    password = "123456"     # 密码

    def show_menu(self):
        """
            显示菜单
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


    def __init__(self, database):
        # 获取数据连接对象
        self.conn:Connection = Connection(host=self.host, port=self.port, user=self.user,
                          password=self.password, autocommit=True)
        self.conn.select_db(database)       # 选择数据库
        self.cursor = self.conn.cursor()    # 获取游标
        self.headline = "学号\t姓名\t班级\t性别\t年龄\t电话\tQQ\t地址"


    # 菜单栏
    def show_menu(self):
        print("*" * 70)
        print("欢迎使用学生管理系统")
        print("1.浏览全部学生信息")
        print("2.新增学生信息")
        print("3.查找学生信息")
        print("4.修改学生信息")
        print("5.删除学生信息")
        print("0.退出系统")
        print("*" * 70)


    # 添加学生信息
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
        sql = f"insert into student(id,name,classed,sex,age,phone,qq,address) values({id},{name},{classed},{sex},{age},{phone},{qq},{address})"
        self.cursor.execute(sql)
        print(f"成功新增{name}学生")

    # 显示所有学生信息
    def show_all(self):

        sql = "select id,name,classed,sex,age,phone,qq,address from student"
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()

        # 元组长度就是学生信息条数
        if len(data_tuple) == 0:
            print("当前没有学生记录，请使用新增功能添加学生信息")
            return
        for line in data_tuple:
            print(f"{line[0]}\t", end='')
            print(f"{line[1]}\t", end='')
            print(f"{line[2]}\t", end='')
            print(f"{line[3]}\t", end='')
            print(f"{line[4]}\t", end='')
            print(f"{line[5]}\t", end='')
            print(f"{line[6]}\t", end='')
            print(f"{line[7]}\t", end='')
            print()


    # 查找姓名为name的学生信息
    def search_student(self, name):
        sql = f"select id,name,classed,sex,age,phone,qq,address from student where name = {name}"

        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()

        # 如果元组的长度等于0，说明不存在姓名为name的学生信息
        if len(data_tuple)  == 0:
            print(f"抱歉，没有找到{name}")
            return

        # 执行到此处，说明姓名为name的学生信息存在
        print(self.headline)
        line = data_tuple[0]
        print(f"{line[0]}\t", end='')
        print(f"{line[1]}\t", end='')
        print(f"{line[2]}\t", end='')
        print(f"{line[3]}\t", end='')
        print(f"{line[4]}\t", end='')
        print(f"{line[5]}\t", end='')
        print(f"{line[6]}\t", end='')
        print(f"{line[7]}\t", end='')
        print()


    # 提示用户输入对应的信息，tip_message是提示信息，返回用户输入的信息
    def input_info(self, old_value, tip_message):
        result = input(tip_message)
        if len(result) > 0:
            return result
        else:
            return old_value

    # 修改学号为id的学生信息
    def update_student(self, id:str):
        print("修改学生信息")
        # 先查找学号为id的学生
        sql = f"select id,name,classed,sex,age,phone,qq,address from student where id = {id}"
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()
        # 判断学号为id的学生是否存在
        if len(data_tuple) == 0:
            print(f"抱歉，不存在学号为{id}的学生")
            return
        # 能执行到此处，说明学号为id的学生存在，修改信息
        data_tuple = data_tuple[0]
        name = self.input_info(data_tuple[0], "姓名：")
        classed = self.input_info(data_tuple[0], "班级：")
        sex = self.input_info(data_tuple[0], "性别：")
        age = int(self.input_info(data_tuple[0], "年龄："))
        phone = self.input_info(data_tuple[0], "电话：")
        qq = self.input_info(data_tuple[0], "QQ：")
        address = self.input_info(data_tuple[0], "地址：")
        sql = f"update student set name={name},classed={classed},sex={sex},age={age},phone={phone},qq={qq},address={address} where id = {id}"
        self.cursor.execute(sql)
        print(f"学号为{id}的学生信息修改成功")


    def delete_student(self, id:str):
        sql = f"delete from student where id = {id}"
        count = self.cursor.execute(sql)
        # 执行修改操作，返回值是修改的数据行数
        if count > 0:
            print(f"成功删除学号为{id}的学生信息")
        else:
            print(f"不存在学号为{id}的学生")







