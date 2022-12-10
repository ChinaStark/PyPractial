class Stu:
    def __init__(self, stuid=None, name=None, sex=None, classname=None, math=None, chinese=None, english=None):
        self.StuId = stuid
        self.Name = name
        self.Sex = sex
        self.ClassName = classname
        self.Math = math
        self.Chinese = chinese
        self.English = english

    def __str__(self):
        return f"student：id={self.StuId},name={self.Name},sex={self.Sex},classname={self.ClassName}," \
               f"math={self.Math},chinese={self.Chinese},english={self.English}"


class User:
    def __init__(self, username, pwd):
        self.Username = username
        self.Password = pwd
