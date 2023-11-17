#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : connectMysql.py
@Author     : Gr%1m
@Date       : 11/11/2023 11:21 pm
"""
import pymysql


def MySQLConnect():
    connection = pymysql.connect(
        host='127.0.0.1',  # IP，MySQL数据库服务器IP地址 后面换成局域网地址
        port=3306,  # 端口，默认3306，可以不输入
        user='dvwa',  # 数据库用户名
        password='p@ssw0rd',  # 数据库登录密码
        database='dvwa',  # 要连接的数据库
        charset='utf8'  # 字符集，注意不是'utf-8'
    )
    return connection


def ReadData():
    # 连接数据库
    conn = MySQLConnect()
    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()
    # 读数据库
    # cursor.execute('select * from test')
    cursor.execute('show global variables like "%general\_log%";')
    aa = cursor.fetchall()
    cursor.execute('show global variables like "secure%";')
    bb = cursor.fetchall()

    print(aa, bb, )
    conn.commit()
    # 关闭游标 关闭数据库连接
    cursor.close()
    conn.close()


ReadData()
