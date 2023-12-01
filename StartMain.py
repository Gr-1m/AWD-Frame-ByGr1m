#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : StartMain.py
@Author     : Gr%1m
@Date       : 10/11/2023 4:33 pm
"""
from Configs.frame_config import *
from cmd import Cmd
from func.CmdColors import printX
from modules.Auxiliary import *
from modules.Scan import *
from modules.Attack import *
from modules.Defense import *
import os, sys, time

try:
    Mode = sys.argv[1].upper()
except IndexError:
    Mode = 'X'

if DEBUG:
    Mode = 'DEBUG'
    from Configs.debug_config import *
elif Mode == 'BUGKU':
    from Configs.bugku_config import *
elif Mode == 'NORMAL':
    from Configs.edit_config import *
elif Mode == 'DEBUG':
    from Configs.debug_config import *
else:
    printX('[-] No This Mode (Normal|Debug|Bugku)\n')
    printX('[!] python StartMain.py [Mode]')
    exit(0)


class AwdConsole(Cmd):
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
        # from importlib import reload
        # todo: Warning
        args = argv.split()
        printX(f'[!] run init will flush all Global Config (Default in FileConfig)')
        printX(f'[+] Init 初始化中')
        # for k in GLOBAL_CONFIG:
        #     del globals()[k]

    def do_show(self, argv):
        args = argv.split()
        if len(argv) < 1:  # or args[0] not in SHOW_CONFIG
            printX("[i] show [all | gi | gti | msi | fi | alive] / Payloads(Pay)")
            return 0
        elif args[0].islower() and args[0] not in SHOW_CONFIG:
            printX(f"[?] do you mean '{args[0][0].upper() + args[0][1:]}' ? Try It")
            return 0

        if args[0] == 'all':
            for k in globals().keys():
                if allow_show(k):
                    print(f"{k}: {globals()[k]}")
        elif args[0] == 'gi':
            print(f"""
            |------------------|---------------------------------------------------------------|
            |   Name           |  Current Setting                                              |
            |------------------|---------------------------------------------------------------|
            | My Team Server   | {MyHost}
            | Enemies Server   | {EyHosts}
            | Flag Token       | {Token}
            | Submit API       | {SubmitAPI}
            | Submit Param     | Token:,Flag:
            | Team Replace Str | {TeamReplaceStr}
            |------------------|---------------------------------------------------------------|
            """)
        elif args[0] == 'gti':
            print(f"""
            |------------------|---------------------------------------------------------------|
            |   Name           |  Current Setting              |
            |------------------|---------------------------------------------------------------|
            | Game Start Time  | \t{GSTime}
            | Round Count      | \t{RCount} rounds
            | Round Time       | \t{RTime}(s) , about {RTime // 60}min
            | Defensive time   | \t{DFTime}(s), about {DFTime // 60}min
            |------------------|---------------------------------------------------------------|
            """)
        elif args[0] == 'msi':
            # todo : debug
            print(f"""
            |------------------|---------------------------------------------------------------
            |   Name           |  Current Setting                                             |
            |------------------|---------------------------------------------------------------
            | SSH Info         | Port: {str(MyHostSSH['Port'])}, User: {MyHostSSH['User']}, Pass: {MyHostSSH['Pass']} NeedChange: {MyHostSSH['NeedChange']}, PassChangeTo: {MyHostSSH['PassChangeTo']}
            | MySQL Info       | Port: {str(MyHostSQL['Port'])}, User: {MyHostSQL['User']}, Pass: {MyHostSQL['Pass']} NeedChange: {MyHostSQL['NeedChange']}, PassChangeTo: {MyHostSQL['PassChangeTo']}
            | Vulner Info      | {Vulner}
            |------------------|---------------------------------------------------------------
            """)
        elif args[0] == 'fi':
            print(f"""
            |------------------|---------------------------------------------------------------|
            |   Name           |  Current Setting                                              |
            |------------------|---------------------------------------------------------------|
            | FLag Path        | '{FlagPath}'
            | Flag Regular     | '{FlagRegular}'
            | Flag Length      | {FlagLen}
            |------------------|---------------------------------------------------------------|
            """)
        elif args[0] == 'alive':
            printX(f'[!] Last scan time was{ScanTime}\nPlease Decide whether to Re-SCAN based on the actual situation')
        elif allow_show(args[0]) and args[0] in globals().keys():
            print(f"{args[0]}: {globals()[args[0]]}")
        elif args[0] in ''.join([_ for _ in globals().keys() if allow_show(_)]):
            for k in [_ for _ in globals().keys() if allow_show(_)]:
                if args[0] in k:
                    print(f"{k}: {globals()[k]}")
        else:
            printX("[-] Not Find this variable")

    def do_set(self, argv):
        args = argv.split('=')[0].split()
        args.append(argv.split('=')[-1])
        keys = globals().keys()
        if len(args) < 3 or args[0] not in ['global', 'g', 'add' 'a']:
            printX(f"[i] -g global, -a add, set -g xxx=xxx, set add Flags flagxx")
        elif args[1] not in keys:
            printX(f"[!] Need at least two param Or Not Find {args[1]}")
            printX(f"[i] you can set the following options\n")
            print([_ for _ in keys if allow_show(_)])
            # 提示设置变量 至少两个参数，并且只能设置非魔法变量且有大写字母的全局变量
            return 0

        if allow_show(args[1]):
            globals()[args[1]] = args[2]
            if args[1] == 'Mode':
                printX(f'[!] Change Mode should do `init`')
        else:
            printX("[-] Not allow change, Read-Only Variable")

    def do_unset(self, argv):
        args = argv.split()
        if len(args) < 1 or args[0] not in globals().keys():
            printX("[!] need at least a param")
            printX("[i] you can unset the following options\n")
            print([_ for _ in globals().keys() if allow_show(_)])
            # 提示设置变量 至少两个参数，并且只能设置非魔法变量且有大写字母的全局变量
            return 0

        if allow_show(args[0]):
            globals()[args[0]] = ''
        else:
            printX("[-] Not allow unset, Read-Only Variable")

    def do_timedown(self, argv=None):
        GSTimestamp = int(time.mktime(time.strptime(GSTime, "%Y-%m-%d %H:%M:%S")))
        if game_start_remind(GSTimestamp, DFTime):
            round_count_remind(GSTimestamp, DFTime, RTime, RCount)
            return 0

    def do_scan(self, argv=''):
        if len(argv) < 1:
            printX("[i] scan [alive | ssh | sql | vul]")
            return 0
        args = argv.split()[:1]
        if args[0] == 'alive':
            try:
                port = args[1]
            except IndexError:
                port = 80
            globals()['EyHosts'] = scan_alive(EyHosts, MyHost, TeamReplaceStr, port)
        elif args[0] == 'ping':
            pass
        elif args[0] == 'ssh':
            pass
        elif args[0] == 'sql':
            pass
        elif args[0] == 'vul':
            pass
        else:
            printX("[-] no this option")

    def do_submit(self, argv=''):
        if len(argv) < 1:
            print("submit [auto|manual flag{x}?]")
            return 0
        args = argv.split()
        from modules.Attack import Flags
        if args[0] == 'auto':
            for flag in Flags:
                result, res_code = submit_flag(SubmitAPI, Token, flag)
                if Mode == 'Bugku':
                    if '恭喜您，Flag正确' in result:
                        printX(f'[+] {flag} is right')
                    elif '请勿重复提交' in result:
                        printX(f'[-] {flag} is repeat')
                elif res_code == 200:
                    printX(f'[+] {flag} is right')
            Flags.clear()

        elif args[0] == '-m' and len(args) > 1:
            flag = args[1]
            result, res_code = submit_flag(SubmitAPI, Token, flag)
            if Mode == 'Bugku':
                if '恭喜您，Flag正确' in result:
                    printX(f'[+] {flag} is right')
                elif '请勿重复' in result:
                    printX(f'[-] {flag} is repeat')
                elif 'Error' in result:
                    printX(f'[-] Error Flag')
                else:
                    printX(f'[!] {flag} please retry to submit !')
            elif res_code == 200:
                printX(f'[+] {flag} is right')

    def do_getflag(self, argv=''):
        try:
            get_flag(EyHosts)
        except KeyboardInterrupt:
            print('\r', end='')
            printX("[!] Quit getflag")
        except Exception as e:
            printX(f"[-] Error {e}")
        else:
            print(Flags)

    def do_check(self, argv=''):
        args = argv.split()
        if len(args) < 1:
            return 0
        if args[0].lower() == 'me':
            self.do_checkme()
            return 0
        # todo:

    def do_checkme(self, argv=''):
        status = check_me(MyHost, AliveStr)
        for host in EyHosts:
            if MyHost in host:
                EyHosts[host] = status.split('m')[1].split('\x1b')[0]
        if 'Alive' in status:
            printX(f'[+] Myself Server is {status}, 200')
        else:
            printX(f'[!] Myself Server is {status}')

    def do_clear(self, argv=''):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_getbackup(self, argv=''):
        save_path = argv.split()[0]
        if os.path.isdir(save_path):
            get_backup(MyHostSSH, save_path)
        else:
            printX(f'[-] no such directory: {save_path}')

    def do_mysql(self, argv=''):
        conn = connect_mysql(MyHostSQL)
        if conn is None:
            printX('[-] Failed to Connect My SQL')
            return 0
        sqlcmd = ''
        while sqlcmd != 'exit':
            try:
                sqlcmd = input("mysql>")
                if sqlcmd == 'help':
                    print(f"\x1b[92m{SQL_HELP} \x1b[0m")
                    continue
                elif sqlcmd[-1] != ';' or ';' not in sqlcmd:
                    printX("[!] Now in SQL cmd, must end with ';' ")
                result = exe_sql(conn, sqlcmd)
                print(result)
            except (KeyboardInterrupt, EOFError):
                printX(f"[!] back to AWD Frame Consoles")
                break
            except Exception as e:
                printX(f"[-] {e.__class__.__name__}: {e}")

        conn.close()

    def do_restart(self, argv=''):
        os.execv(sys.executable, ['python'] + sys.argv)

    # todo : Test
    def do_test(self, argv=''):
        pass
        # todo:
        # from importlib import reload
        # reload(sys.modules['modules.Attack'])
        # print(sys.modules['Configs.debug_config'])
        # printX(f"[+] def ")
        # del sys.modules['Configs.debug_config']

        # for k in globals().keys():
        #     if '__' not in k and k[0].isupper() and not k.isupper() and k not in NOT_SHOW:
        #         print(f"'{k}',", end='')

    def do_exit(self, argv=''):
        # todo : write in file
        exit(0)


if __name__ == '__main__':
    try:
        console = AwdConsole()
        os.environ['TERM'] = 'xterm-color'
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        console.cmdloop()
    except (KeyboardInterrupt, EOFError):
        printX("[+] \n exit")
        # printX("[+] Interrupt: use the 'exit' command to quit")
        exit(0)
    except Exception as e:
        printX(f"[-] {e.__class__.__name__} {e}")
        exit(1)
