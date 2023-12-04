#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : config.py
@Author     : Gr%1m
@Date       : 4/12/2023 10:59 am
"""
# About Game Info
TeamReplaceStr = 'XXXTrs'
MyHost = "192.168.122.1"
EyHosts = f"192.168.122.{TeamReplaceStr}"
Token = "test_token1"

API_URL = 'http://kaming/awduse/submit.php'
API_token = 'token'
API_flag = 'flag'
API_method = 'GET'
# SubmitAPI = [URL, token的参数, flag的参数, method], GET: http://????.com/xxx/submit.php?token=111Token1111&flag=Cflag{xxx}
SubmitAPI = [API_URL, API_token, API_flag, API_method]

# About Game Time Info
GSTime = "2023-12-03 19:00:00"  # Game Start Time
RTime = 600  # Round Time
RCount = 20  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://msfadmin:msfadmin@{MyHost}:22/var/www/dvwa'
MyHostSQL = f'mysql://root:@{MyHost}:3306/cms'

# Server Vulnerable Info
Vulner = {
    # Attack type: f'scheme://language@host:port/path'
    'Web1': f'http://php@xxx:80/app/index.php',
    'Web2': f'http://python@xxx:8000/var/www/html/index',
    'Pwn0': f'pwn://c++@xxx:4444/home/ctf/pwn',
}

# About Flag
FlagPath = '/flag'
FlagRegular = r'flag{\w{32}}'
