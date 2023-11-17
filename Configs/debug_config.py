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
MyHost = "192.168.122.231"
EyHosts = f"192.168.122.{TeamReplaceStr}"
Token = "test_token1"

API_URL = 'http://kaming/awduse/submit.php'
API_token = 'token'
API_flag = 'flag'
API_method = 'GET'
# SubmitAPI = [URL, token的参数, flag的参数, method], GET: http://????.com/xxx/submit.php?token=111Token1111&flag=Cflag{xxx}
SubmitAPI = [API_URL, API_token, API_flag, API_method]

# About Game Time Info
GSTime = "2023-11-13 20:00:00"  # Game Start Time
RTime = 300  # Round Time
RCount = 20  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://msfadmin:msfadmin@{MyHost}:22/xx'
MyHostSQL = f'mysql://cms:qwerty;@{MyHost}:3306/xx'

# MyHost.split(':')
# [0] protocol [1] //username [2]password@MyhostIP [3]port/xx


# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
