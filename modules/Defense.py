#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Defense.py
@Author     : Gr%1m
@Date       : 14/11/2023 11:00 am
"""
from urllib.parse import urlparse as URL
import requests
import paramiko
import pymysql

Vulner = {
    # Attack type: [port, language, path]
    'Web1': [80, 'php', '/app/'],
    'Web2': [8000, 'python', '/var/www/html/'],
    'Pwn0': [4444, '', '/home/ctf/pwn'],
    'Test': [80, 'test', 'home/usetest/filestp/testfile']
}
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'


# Reinforcement stage
def check_me(my_host, alive_str):
    try:
        res = requests.get(url=f"http://{my_host}/")
        if alive_str in res.text:
            return '\x1b[01;32mAlive\x1b[0m'
        elif res.status_code == 200:
            return '\x1b[01;33mNoAliveStr\x1b[0m'
        else:
            return '\x1b[01;33mNot 200\x1b[0m'
    except KeyboardInterrupt:
        print('[!] Check Myself Stop')
        return '\x1b[01;33mUnknown\x1b[0m'
    except Exception:
        return '\x1b[01;31mDown\x1b[0m'


def get_backup(myhostssh, webroot):
    backup_filename = 'www.tar'

    try:
        client = connect_ssh(myhostssh)
        print(f"[+] connect Host {myhostssh.hostname}")

        _, stdout, stderr = client.exec_command('pwd')
        pwd = stdout.read().decode().strip()
        _, stdout, stderr = client.exec_command(f"echo '<!--{AliveStr}-->'; >> {webroot}/index.php")
        _, stdout, stderr = client.exec_command(f'tar -zcvf {backup_filename} {webroot}')
        print(f"[+] tar WebRoot directory {webroot} success, sftp get {backup_filename}")

        sftp = client.open_sftp()
        sftp.get(f"{pwd}/{backup_filename}", "data/www.tar")
        sftp.close()
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f'[-] SSH Error: {e}')
    except FileNotFoundError as e:
        print(f'[-] FileNotFoundError: {e}, {stderr.read().decode()}')
    else:
        print(f"[+] download finished -> ./data/{backup_filename}")
    finally:
        client.close()
        return 0


def connect_ssh(myhostssh):
    # 设置目标机器的SSH连接信息

    # 创建SSH客户端 自动添加服务器的SSH密钥（这将绕过密钥验证，仅在信任网络中使用）
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接到目标机器
    myhostssh = URL(myhostssh)
    try:
        client.connect(hostname=myhostssh.hostname,
                       username=myhostssh.username,
                       password=myhostssh.password,
                       port=myhostssh.port, )

    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f'[-] SSH Error: {e}')
    else:
        return client


def connect_mysql(myhostsql):
    myhostsql = URL(myhostsql)
    try:
        server = {'host': myhostsql.hostname,
                  'port': myhostsql.port,
                  'user': myhostsql.username,
                  'password': myhostsql.password,
                  'charset': 'utf8',  # 字符集，注意不是'utf-8'
                  }
        print(f"\x1b[01;32m[+]\x1b[0m Wait For, connecting to {server['user']}@{server['host']}")
        print(f"[T] Use the\x1b[01;32m 'help'\x1b[0m to view Tips!")
        conn = pymysql.connect(**server)

    except pymysql.OperationalError as e:
        print(f"[-] {e.__class__.__name__} {e}")
    else:
        return conn


def exe_sql(conn, sqlcmd):
    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()
    try:
        cursor.execute(sqlcmd)
        stdout = cursor.fetchall()
        # 提交事务 关闭游标
    except Exception as e:
        print(f"[-] {e.__class__.__name__} {e}")
        conn.rollback()
    else:
        conn.commit()
        cursor.close()
        return stdout
