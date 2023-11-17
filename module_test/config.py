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
MyHost = "192-168-1-237.pvp3459.bugku.cn"
EyHosts = f"192-168-1-{TeamReplaceStr}.pvp3459.bugku.cn"
Token = "45e2336849327799792041a395ec5e68"
SubmitAPI = f"https://ctf.bugku.com/pvp/submit.html?token={Token}&flag={TeamReplaceStr}"

# About Game Time Info
GSTime = "2023-11-17 17:30:00"  # Game Start Time
RTime = 300  # Round Time
RCount = 20  # Round Count
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
FlagPath = ['/flag', '/flag.txt']
FlagFormat = 'flag{xxxx_xxxx_xxxx}'
FlagRegular = r'^flag{(\w+|_)+}$'
BUGKU_FLAG_LEN = 32
FlagLen = BUGKU_FLAG_LEN


# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
AppendStr = f'echo "<!--{AliveStr}-->";'
