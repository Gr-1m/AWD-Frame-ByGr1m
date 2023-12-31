#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : frame_config.py
@Author     : Gr%1m
@Date       : 11/11/2023 1:02 pm
"""
import os as _os
from cmd import Cmd as _Cmd

DEBUG = False

TITLE = "AWD-Frame-ByGr%1m"
AUTHOR = "Gr%1m"
AUTHOR_EMAIL = "1299091518@qq.com"
AUTHOR_BLOG = "https://blog.enxm.top/"  # 自签名证书 可放心无视风险

VERSION = "V1.0.6"
UPDATE_DATE = "2023-12-08"

# 提示符
PROMPT = '\x1b[01;49;46mAWD-FOR-Gr%1m\x1b[0m-> '
# 欢迎信息 长信息
WELCOME = f"""
                ########## AWD-Farmwork-V1.0.3 #################
                                                        Powered By {AUTHOR} 
                                                        Date:{UPDATE_DATE}   
                                                    
    1. 本框架用于AWD比赛使用，在禁止使用WAF的比赛中，请勿将本框架和WAF结合，因此造成后果作者不承担任何责任
    2. """

URL_HELP = """
    本脚本中的一切 URL,都遵循格式：scheme://username:password@hostname:port/path?query1=xxx&query2=xxx
    例如1 : SubmitAPI = "https://ctf.bugku.com/pvp/submit.html?token=xxx&flag=xxx"
    例如2 : ssh_url = "ssh://team1:abc123@192.168.1.1:2222/"
    例如3 : payload = "POST://bugku.com:80/game/index.php?a=phpinfo();" "php://xxxx.org:8081/config/xx.php?s=s"
    """

CMD_HELP = """
    Command Tips
    ===================
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | init             | 初始化(清空靶机ip列表)
            | show             | 比赛初始化的配置信息
            | set              | 初始化(清空靶机ip列表)
            | scan             | 扫描存活主机，数据库，弱点
            |------------------|---------------------------------------------------------------|
    
    Attack Module Tips
    ===================
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | getflag          | 执行获取Flag
            | submit           | 扫描存活主机，数据库，弱点
            | shellin          | 植入后门
            |------------------|---------------------------------------------------------------|
   
    Defense Module Tips
    ===================
            |------------------|---------------------------------------------------------------|
            |   Command        |  Description                                                  |
            |------------------|---------------------------------------------------------------|
            | getbackup        | 获取打包的网站源码
            | submit           | 扫描存活主机，数据库，弱点
            | shellin          | 植入后门
            |------------------|---------------------------------------------------------------|
            """
SQL_HELP = """
            |-------------------------------------------------------------------|-------------------|
            |                       SQL Command                                 |  Description      |
            |-------------------------------------------------------------------|-------------------|
            | 1: show global variables like "general%";                         | 查看日志记录配置信息
            | 2: show global variables like "secure%";                          | 查看系统调用信息
            | 3: create user 'username'@'localhost' identified by 'password';   | 创建用户
            | 4: set password for username=password('1234');                    | 修改密码
            | 5: flush privileges;                                              | 刷新权限
            |------------------|------------------------------------------------|-------------------|
"""
NOT_SHOW = ['XCmd', 'AwdConsole', 'Intro', 'AliveFirst', 'ProgressBar']
INIT_CHECK = ['']
SHOW_CONFIG = ['all', 'gi', 'gti', 'msi', 'fi', 'alive']
GLOBAL_CONFIG = ['TeamReplaceStr', 'MyHost', 'EyHosts', 'Token', 'APIMethod', 'SubmitAPI', 'GSTime', 'RTime', 'RCount',
                 'DFTime', 'MyHostSSH', 'MyHostSQL', 'Vulner', 'FlagPath', 'FlagFormat', 'FlagRegular', 'FlagLen',
                 'AliveStr', 'AliveTime', 'AppendStr', ]

FRAME_DIR = _os.path.dirname(_os.path.dirname(__file__))


class XCmd(_Cmd):
    prompt = PROMPT
    Object = None

    def __init__(self):
        super().__init__()
        self.Welcome = WELCOME
        self.commandHelp = CMD_HELP

        print(f'\x1b[93m{self.Welcome} \x1b[0m')
        print(f'\x1b[92m{self.commandHelp} \x1b[0m')

    def preloop(self):
        pass

    def parseline(self, line):
        line = line.strip()
        if not line:
            return None, None, line
        elif line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars:
            i += 1
        cmd, arg = line[:i], line[i:].strip().split()
        return cmd, arg, line

    def emptyline(self) -> bool:
        # if self.lastcmd:
        #     return self.onecmd(self.lastcmd)
        pass  # 解决空输入 自动上一条指令的问题


def clear():
    _os.environ['TERM'] = 'xterm-color'
    if _os.name == 'nt':
        _os.system('cls')
    else:
        _os.system('clear')


def allow_show(key):
    format_bool = key[0].isupper() and not key.isupper()
    ignore_bool = '__' not in key and 'Replace' not in key
    return format_bool and ignore_bool and key not in NOT_SHOW
    # return '__' not in key and key[0].isupper() and not key.isupper() and key not in NOT_SHOW
