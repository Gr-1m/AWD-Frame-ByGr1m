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
EyHosts = f"192-168-1-{TeamReplaceStr}.pvp3487.bugku.cn"
Token = "e430ec6d4fe99be8e70a9e63a0a8af45"

APIMethod = 'GET'
SubmitAPI = [f"https://ctf.bugku.com/pvp/submit.html", 'token', 'flag', APIMethod]

# About Game Time Info
GSTime = "2023-11-14 20:30:00"  # Game Start Time
RTime = 300  # Round Time
RCount = 15  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://team5:sshpasswd@{MyHost}:2222/'
MyHostSQL = f'mysql://cms:cmspasswd;@{MyHost}:3306/cms'

Vulner = {
    # Attack type: [port, language, path]
    'Web1': [80, 'php', '/app/'],
    'Web2': [8000, 'python', '/var/www/html/'],
    'Pwn0': [4444, '', '/home/ctf/pwn'],
}

# About Flag
FlagPath = '/flag'
FlagFormat = 'flag{xxxx_xxxx_xxxx}'
FlagRegular = r'^flag{\w{32}}$'
BUGKU_FLAG_LEN = 32
FlagLen = BUGKU_FLAG_LEN

# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
AppendStr = f'echo "<!--{AliveStr}-->";'
