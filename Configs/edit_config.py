#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : debug_config.py
@Author     : Gr%1m
@Date       : 10/11/2023 10:03 pm
"""
# About Game Info
TeamReplaceStr = 'XXXTrs'
MyHost = "192-168-1-187.pvp3487.bugku.cn"
EyHosts = f"192.168.122.{TeamReplaceStr}"
Token = "45e2336849327799792041a395ec5e68"

API_URL = 'http://kaming/awduse/submit.php'
API_token = 'token'
API_flag = 'flag'
API_method = 'GET'
# SubmitAPI = [URL, token的参数, flag的参数, method], GET: http://????.com/xxx/submit.php?token=111Token1111&flag=Cflag{xxx}
SubmitAPI = [API_URL, API_token, API_flag, API_method]

# About Game Time Info
GSTime = "2024-01-10 20:30:00"  # Game Start Time
RTime = 300  # Round Time
RCount = 15  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = {
    'Port': 2222,
    'User': 'team5',
    'Pass': 'xxxxxxxxxxxx password',
    'NeedChange': False,
}
MyHostSQL = {
    'Port': 3306,
    'User': 'cms',
    'Pass': 'xxxxxxxxxxxx password',
    'Database': 'cms',
    'NeedChange': True,
}

Vulner = {
    # Attack type: [port, language, path]
    'Web1': [80, 'php', '/app/'],
    'Web2': [8000, 'python', '/var/www/html/'],
    'Pwn0': [4444, '', '/home/ctf/pwn'],
}

# About Flag
FlagPath = '/flag'
FlagFormat = 'flag{xxxx_xxxx_xxxx}'
FlagRegular = r'flag{(\w|-){35}}'
FlagLen = 35

# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
AppendStr = f'echo "<!--{AliveStr}-->";'
