from pymysql import Connection
from WorkTwo.POJO import User, Stu


def getConnection() -> Connection:
    """获取数据库连接对象"""
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="4aea6030",
        autocommit=True
    )
    return conn


def loginCheck(user: User) -> bool:
    """判断User的账号密码是否正确"""
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = f"select username,password from user where username = '{user.getUsername()}' and password = '{user.getPassword()}'"
    count = cursor.execute(sql)
    if count > 0:
        return True
    else:
        return False


def selectAll() -> list:
    """查询全部学生信息，如果没有返回空列表"""
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    data_tuple = cursor.fetchall()
    studentList = list()
    for data in data_tuple:
        print(data)
        student = Stu(stuid=data[0], name=data[2], sex=data[1], classname=data[3], math=data[4], chinese=data[5],
                      english=data[6])
        studentList.append(student)

    return studentList


def selectOne(id) -> list[Stu]:
    """根据学号查询学生信息，如果没有返回空列表"""
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = f"select * from student where id = '{id}'"
    cursor.execute(sql)
    data_tuple = cursor.fetchall()
    studentList = list()
    for data in data_tuple:
        student = Stu(stuid=data[0], name=data[1], sex=data[2], classname=data[3], math=data[4], chinese=data[5],
                      english=data[6])
        studentList.append(student)

    return studentList


def update(id, student: Stu) -> bool:
    """根据学号修改学生信息，如果修改成功返回True，否则返回False"""
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = f"update student set name='{student.Name}',sex='{student.Sex}'," \
          f"classname={student.ClassName},math={student.Math}," \
          f"chinese={student.Chinese},english={student.English} where id='{id}'"
    count = cursor.execute(sql)
    return True if count > 0 else False


def insert(student: Stu):
    """如果学生学号存在，不插入，如果学号不存在，插入学生信息，插入成功返回True，否则返回False"""
    count = len(selectOne(student.StuId))
    if count > 0:
        return False
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = f"insert into student values('{student.StuId}','{student.Name}'," \
          f"'{student.Sex}','{student.ClassName}','{student.Math}','{student.Chinese}'," \
          f"'{student.English}')"
    count = cursor.execute(sql)
    return True if count > 0 else False


def delete(id) -> bool:
    """如果学生学号存在，删除学生信息，并且返回True；如果学号不存在，则返回False"""
    conn = getConnection()
    conn.select_db("python")
    cursor = conn.cursor()
    sql = f"delete from student where id='{id}'"
    count = cursor.execute(sql)
    return True if count > 0 else False
