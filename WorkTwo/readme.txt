数据库名：python

user数据库表
    username字段      varchar(255)
    password字段      varchar(255)

    建表语句：
    create table if not exists user(
        username varchar(255),
        password varchar(255)
    );

Student数据库表
    id              varchar(255)
    name            varchar(255)
    sex             varchar(255)
    classname       int
    math            double
    chinese         double
    english         double

    建表语句：
    create table if not exists user(
        id varchar(255),
        sex varchar(255),
        name varchar(255),
        classname varchar(255),
        math varchar(255),
        chinese varchar(255),
        english varchar(255),
    );


