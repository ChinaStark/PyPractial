学生管理系统1.1
    通过读取文件进行学生信息的增删改查
    读写文件文件名：student.txt
    列表存放学生信息：card_list
    学生类，每一个Student对象保存一个学生信息

    函数说明：
        load_info()：从文件中导入学生信息，将文件中的学生信息保存到列表中
        save_info()：将列表中数据保存到文件中
        show_menu()：显示菜单
        new_student()：新增学生，通过输入语句读取用户信息保存到列表中
        show_all()：将列表中所有信息显示出来
        search_student()：查找列表中指定的信息
        update_student()：修改列表中指定的信息
        input_info(dict_value, tip_message)：根据提示信息，用户输入对应信息
        delete_student()：删除列表中学生信息

