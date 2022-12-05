

class Student:
    """
        学生类，用来保存一个学生信息
    """
    def __init__(self, id:str, name:str, classed:int,
                 sex:str, age:int, phone:str, qq:str, address:str):
       self.id = id                 # 学生学号
       self.name = name             # 学生姓名
       self.classed = classed       # 学生班级
       self.sex = sex               # 学生性别
       self.age = age               # 学生年龄
       self.phone = phone           # 学生电话
       self.qq = qq                 # 学生QQ
       self.address = address       # 学生地址
