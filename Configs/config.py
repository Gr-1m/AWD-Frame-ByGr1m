#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : config.py
@Author     : Gr%1m
@Date       : 4/12/2023 10:59 am
"""
# About Game Info
TeamReplaceStr = 'TEAM_HOST_REPLACE'
MyHost = "192-168-1-39.pvp3610.bugku.cn"
EyHostExample = f"192.168.122.{TeamReplaceStr}"
EyHosts = {}
Token = "test_token1"

API_URL = 'http://kaming/awduse/submit.php'
API_token = 'token'
API_flag = 'flag'
API_method = 'GET'
# SubmitAPI = [URL, token的参数, flag的参数, method], GET: http://????.com/xxx/submit.php?token=111Token1111&flag=Cflag{xxx}
SubmitAPI = [API_URL, API_token, API_flag, API_method]

# About Game Time Info
GSTime = "2023-12-09 19:00:00"  # Game Start Time
RTime = 600  # Round Time
RCount = 20  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://msfadmin:msfadmin@{MyHost}:2222/var/www/html'
MyHostSQL = f'mysql://root:@{MyHost}:3306/cms'

# Server Vulnerable Info
Vulner = {
    # Attack type: f'scheme://language@host:port/path'
    'Web1': f'http://php@{TeamReplaceStr}:80/var/www/html/index.php',
    'Web2': f'http://python@{TeamReplaceStr}:8000/var/www/html/index',
    'Pwn0': f'pwn://c++@xxx:4444/home/ctf/pwn',
}

# About Flag
FlagPath = '/flag'
FlagRegular = r'flag{\w{32}}'
