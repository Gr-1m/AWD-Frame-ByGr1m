#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : AwdConsole.py
@Author     : Gr%1m
@Date       : 17/11/2023 3:38 pm
"""
from Configs.frame_config import *
from func.CmdColors import printX
from cmd import Cmd
import os, sys


class AwdCmd(Cmd):
    prompt = PROMPT
    Object = None

    def __init__(self):
        Cmd.__init__(self)
        self.Welcome = WELCOME
        self.commandHelp = CMD_HELP
        self.intro = f'Welcome to the AWD console. Type help or ? to list commands.\n\x1b[93m Now in {Mode} Mode\x1b[0m'

    def preloop(self):
        print(f'\x1b[93m{self.Welcome} \x1b[0m')
        print(f'\x1b[92m{self.commandHelp} \x1b[0m')

    def precmd(self, line):
        """Hook method executed just before the command line is
        interpreted, but after the input prompt is generated and issued.

        """
        # todo: time flush
        return line

    def help_show(self):
        printX(f"[i] show [all | gi | gti | msi | fi | myalive | eyalive]")
        printX(f"[i] You Also can Input a Part of global.key to View them")
        print(f"   \x1b[01;31m The First letter must be A Upper !! 首字母一定要大写 !\x1b[0m")
        print(f"""
    Example : 
        -> show My
            MyHost: 127.0.0.1
            MyHostSSH: ssh://XXXXXXXXX
            MyHostSQL: XXXXXXXXXXX
        -> show Time
            ScanTime: 
            GSTime: 2023-11-13 20:00:00
            RTime: 300
            DFTime: 1800
            AliveTime: 10
        """)

    def do_init(self, argv):
        from importlib import reload
        # todo: Warning
        args = argv.split()
        printX(f'[!] run init will flush all Global Config (Default in FileConfig)')
        printX(f'[+] Init 初始化中')
        # for k in GLOBAL_CONFIG:
        #     del globals()[k]

    def do_clear(self, argv=''):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # todo : Test
    def do_test(self, argv=''):
        from importlib import reload
        # reload(sys.modules['modules.Attack'])
        print(sys.modules['Configs.debug_config'])
        printX(f"[+] def ")
        del sys.modules['Configs.debug_config']

        # todo:

        # for k in globals().keys():
        #     if '__' not in k and k[0].isupper() and not k.isupper() and k not in NOT_SHOW:
        #         print(f"'{k}',", end='')
