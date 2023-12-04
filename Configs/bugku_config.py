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
MyHost = "192-168-1-229.pvp3589.bugku.cn"
EyHosts = f"192-168-1-{TeamReplaceStr}.pvp{MyHost.split('pvp')[-1].split('.')[0]}.bugku.cn"
Token = "d368301a8d26ea8f0a9ea8b3a2a3ab91"

APIMethod = 'GET'
SubmitAPI = [f"https://ctf.bugku.com/pvp/submit.html", 'token', 'flag', APIMethod]

# About Game Time Info
GSTime = "2023-12-04 8:00:00"  # Game Start Time
RTime = 600  # Round Time
RCount = 20  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://team1:21d54a28983e188044de38870b3baebb@{MyHost}:2222/'
MyHostSQL = f'mysql://cms:bd81904ab8b3bc91@{MyHost}:3306/cms'

Vulner = {
    # Attack type: [port, language, path]
    'Web1': [80, 'php', '/app/'],
    'Web2': [8000, 'python', '/var/www/html/'],
    'Pwn0': [4444, '', '/home/ctf/pwn'],
}

# About Flag
FlagPath = '/flag'
FlagFormat = 'flag{xxxx_xxxx_xxxx}'
FlagRegular = r'flag{\w{32}}'
BUGKU_FLAG_LEN = 32
FlagLen = BUGKU_FLAG_LEN

# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
