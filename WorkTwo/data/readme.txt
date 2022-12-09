数据库名：python
create database python;

user数据库表
    username字段      varchar(15)
    password字段      varchar(15)

    建表语句：
    create table if not exists user(
        username varchar(15),
        password varchar(15)
    );

Student数据库表
    id              varchar(10)
    name            varchar(10)
    sex             varchar(10)
    classname       int
    math            double
    chinese         double
    english         double

    建表语句：
    create table if not exists user(
        id varchar(10),
        sex varchar(2),
        name varchar(10),
        classname varchar(10),
        math varchar(10),
        chinese varchar(10),
        english varchar(10),
    );


