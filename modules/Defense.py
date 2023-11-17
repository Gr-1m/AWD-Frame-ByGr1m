#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Defense.py
@Author     : Gr%1m
@Date       : 14/11/2023 11:00 am
"""
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


def get_backup(myhostssh, webroot='/var/www/twiki/pub'):
    # 设置目标机器的SSH连接信息

    # 创建SSH客户端 自动添加服务器的SSH密钥（这将绕过密钥验证，仅在信任网络中使用）
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接到目标机器
    # MyHostSSH = f'ssh://msfadmin:msfadmin@192.168.122.231:22/x'
    # myhostssh = MyHostSSH
    backup_filename = 'www.tar'
    try:
        client.connect(hostname=myhostssh.split('@')[1].split(':')[0],
                       port=int(myhostssh.split(':')[-1].split('/')[0]),
                       username=myhostssh.split(':')[1][2:],
                       password=myhostssh.split(':')[2].split('@')[0])
        print(f"[+] connect Host {myhostssh.split('@')[1].split(':')[0]}")

        _, stdout, stderr = client.exec_command('pwd')
        pwd = stdout.read().decode().strip()
        _, stdout, stderr = client.exec_command(f'tar -zcvf {backup_filename} {webroot}')
        print(f"[+] tar WebRoot directory {backup_filename} success, sftp get {backup_filename}")

        sftp = client.open_sftp()
        sftp.get(f"{pwd}/{backup_filename}", "data/www.tar")
        sftp.close()
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f'[-] SSH Error: {e}')
    except FileNotFoundError as e:
        print(f'[-] FileNotFoundError: {e}, {stderr.read().decode()}')
    finally:
        print(f"[+] download finished -> ./data/{backup_filename}")
        client.close()
        return 0


def connect_mysql(myhostsql):
    try:
        server = {'host': myhostsql.split('@')[1].split(':')[0],
                  'port': int(myhostsql.split(':')[-1].split('/')[0]),
                  'user': myhostsql.split(':')[1][2:],
                  'password': myhostsql.split(':')[2].split('@')[0],
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
        conn.rollback()
    else:
        conn.commit()
        cursor.close()
        return stdout
