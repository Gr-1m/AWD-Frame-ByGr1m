#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : connectSSH.py
@Author     : Gr%1m
@Date       : 10/11/2023 9:13 pm
"""
import paramiko
# from Configs.config import MyHostSSH

# 设置目标机器的SSH连接信息

# 创建SSH客户端
client = paramiko.SSHClient()
# 自动添加服务器的SSH密钥（这将绕过密钥验证，仅在信任网络中使用）
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到目标机器
client.connect('192.168.122.231', 22, username='msfadmin', password='msfadmin')

# 执行命令
stdin, stout, stderr = client.exec_command('pwd')
print(stout.read().decode())
# 在目标机器上执行命令以获取文件
# 示例：获取/etc/passwd文件并将其保存到本地
# sftp = client.open_sftp()
# sftp.get("/var/www/html/index.php", "passwd_from_target_machine")
# sftp.close()

# 断开连接
client.close()
