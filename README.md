# PyPractial

## 2022-12-1 for python practice training

2022-12-5 compete the WOrkOne
now starting the workTwo

#主要功能
    数据的增删改查
    matplotlib画图，显示成绩的统计信息

##建表语句
###用户表
    create table if not exists user(
        username varchar(15),
        password varchar(15)
    );
###数据表
    create table if not exists student(
        id varchar(10),
        sex varchar(2),
        name varchar(10),
        classname varchar(10),
        math varchar(10),
        chinese varchar(10),
        english varchar(10)
    );
##数据集
    |202001	|女	|andy	|音乐	    |89	|89	|100|
    |202002	|女	|annd	|音乐	    |78	|89	|100|
    |202003	|男	|jhon	|计算机	    |96	|98	|78|
    |202004	|女	|cindy	|英语	    |60	|60	|98|
    |202005	|男	|Denisy	|数学	    |98	|86	|65|
    |202006	|女	|cancy	|英语	    |80	|70	|98|
    |202010	|男	|polo	|计算机	    |98	|99	|60|
    |202007	|女	|rose	|音乐	    |59	|98	|99|
    |202008	|男	|frank	|环境设计   |10	|10	|10|
    |202009	|女	|luycy	|环境设计   |20	|70	|82|