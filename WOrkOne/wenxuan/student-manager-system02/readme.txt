学生管理系统2.1
    通过操作数据库进行学生信息的增删改查
    需要下载pymysql第三方包
    操作的数据库名：python-student
        创建数据库：python
        创建数据库表：student
            id      varchar(255)
            name    varchar(255)
            classed int
            age     varchar(255)
            age     int
            phone   varchar(255)
            qq      varchar(255)
            address varchar(255)

        创建数据库表的语句：
            create table if not exists student(
                id varchar(255),
                name varchar(255),
                classed int,
                age varchar(255),
                phone varchar(255),
                qq varchar(255),
                address varchar(255)
            );

    函数说明：
        show_menu()：显示菜单
        new_student()：新增学生，通过输入语句读取用户信息保存到数据库表中
        show_all()：将数据库表中中所有信息显示出来
        search_student()：查找数据库表中指定的信息
        update_student()：修改数据库表中指定的信息
        input_info(dict_value, tip_message)：根据提示信息，用户输入对应信息
        delete_student()：删除数据库表中学生信息

