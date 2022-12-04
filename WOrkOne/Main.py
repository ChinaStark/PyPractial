import MyfuntionsOne as f

f.load_info()

print("学生信息已导入！")

while True:
    f.show_menu()  # 显示菜单
    action_str = input("请选择希望执行的操作: ")
    print("你选择的操作是 %s" % action_str)
    if action_str in ["1", "2", "3", "4", "5", "6"]:
        if action_str == "1":
            f.show_all()
        elif action_str == "2":
            f.new_student()
        elif action_str == "3":
            f.search_student()
        elif action_str == "4":
            f.update_student()
        elif action_str == "5":
            f.delete_student()
        elif action_str == "6":
            f.save_info()
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【学生信息管理系统】:")
        break
    else:
        print("输入错误，请重新输入:")
