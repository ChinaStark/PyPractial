# 主程序，可以调用student_data模块中的方法

from student_operation import StudentDaoImpl
path = "E:/大学学习/Python/code/library-manager-system/WOrkOne/wenxuan/library-manager-system01/student.txt"
studentDao = StudentDaoImpl(path)



# 执行主程序
while True:
    studentDao.show_menu()      # 显示主菜单
    action = input("请输入你的选择：")
    if action in ["1", "2", "3", "4", "5", "6"]:
        if action == "1":
            studentDao.show_all()
        elif action == "2":
            studentDao.new_student()
        elif action == "3":
            name = input("请输入你要查找学生的姓名：")
            studentDao.search_student(name)
        elif action == "4":
            id = input("请输入要修改学生的学号：")
            studentDao.update_student(id)
        elif action == "5":
            id = input("请输入要删除学生的学号：")
            studentDao.delete_student(id)
        elif action == "6":
            studentDao.save_info()
    elif action == "0":
        print("欢迎再次使用学生管理系统：")
        break
    else:
        print("输入错误，请再次输入：")

