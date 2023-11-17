#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : frame_config.py
@Author     : Gr%1m
@Date       : 11/11/2023 1:02 pm
"""
DEBUG = True

TITLE = "AWD-Frame-ByGr%1m"
AUTHOR = "Gr%1m"
AUTHOR_EMAIL = "1299091518@qq.com"
AUTHOR_BLOG = "https://blog.enxm.top/"  # 自签名证书

VERSION = "V1.0.1"
UPDATE_DATE = "2023-11-14"

# 提示符
PROMPT = '\x1b[01;49;46mAWD-FOR-Gr%1m\x1b[0m-> '
# 欢迎信息 长信息
WELCOME = f"""
                ########## AWD-Farmwork-V1.0.1 #################
                                                        Powered By {AUTHOR} 
                                                        Date:{UPDATE_DATE}   
                                                    
    1. 本框架用于AWD比赛使用，在禁止使用WAF的比赛中，请勿将本框架和WAF结合，因此造成后果作者不承担任何责任
    2.

       """
CMD_HELP = """
    Command Tips
    =============
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | init             | 初始化(清空靶机ip列表)
            | show             | 比赛初始化的配置信息
            | set              | 初始化(清空靶机ip列表)
            | scan             | 扫描存活主机，数据库，弱点
            |------------------|---------------------------------------------------------------|
            
    Attack Module Tips
    =============
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | getflag          | 执行获取Flag
            | submit           | 扫描存活主机，数据库，弱点
            | shellin          | 植入后门
            |------------------|---------------------------------------------------------------|
            
    Defense Module Tips
    =============
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | getflag          | 执行获取Flag
            | submit           | 扫描存活主机，数据库，弱点
            | shellin          | 植入后门
            |------------------|---------------------------------------------------------------|
            """

NOT_SHOW = ['Cmd', 'AwdConsole']
INIT_CHECK = ['']
SHOW_CONFIG = ['all', 'gi', 'gti', 'msi', 'fi', 'alive']
GLOBAL_CONFIG = ['TeamReplaceStr', 'MyHost', 'EyHosts', 'Token', 'APIMethod', 'SubmitAPI', 'GSTime', 'RTime', 'RCount',
                 'DFTime', 'MyHostSSH', 'MyHostSQL', 'Vulner', 'FlagPath', 'FlagFormat', 'FlagRegular', 'FlagLen',
                 'AliveStr', 'AliveTime', 'AppendStr', ]


def allow_show(key):
    return '__' not in key and key[0].isupper() and not key.isupper() and key not in NOT_SHOW
