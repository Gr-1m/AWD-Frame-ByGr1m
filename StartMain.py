#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : StartMain.py
@Author     : Gr%1m
@Date       : 10/11/2023 4:33 pm
"""
import os
import sys
import time

from Configs.frame_config import *
from Configs.config import *
from modules.Attack import *
from modules.Auxiliary import *
from modules.Defense import *
from modules.Persistence import *

try:
    Mode = sys.argv[1].upper()
except IndexError:
    Mode = 'X'

if DEBUG or Mode == 'DEBUG':
    Mode = 'DEBUG'
    MyHost = '192.168.122.231'
    MyHostSSH = f'ssh://msfadmin:msfadmin@{MyHost}:22/var/www/index.php'
    MyHostSQL = f'mysql://root:@{MyHost}:3306/cms'
# elif os.path.isfile(''):  todo: `read cache` or `read sql`
elif Mode == 'BUGKU':
    MyHost = MyHost if 'pvp' in MyHost else "192-168-1-229.pvp3589.bugku.cn"
    EyHostExample = f"192-168-1-{TeamReplaceStr}.pvp{MyHost.split('pvp')[-1].split('.')[0]}.bugku.cn"
    SubmitAPI = [f"https://ctf.bugku.com/pvp/submit.html", 'token', 'flag', 'GET']
    FlagRegular = r'flag{\w{32}}'
elif Mode == 'NORMAL':
    pass
else:
    printX('[-] No This Mode (Normal|Debug|Bugku)\n')
    printX('[!] python StartMain.py [Mode]')
    exit(0)

Intro = f'Welcome to the AWD console. Type help or ? to list commands.\n\x1b[93m Now in {Mode} Mode\x1b[0m'


class AwdConsole(XCmd):
    prompt = PROMPT
    Object = None

    def __init__(self):
        super().__init__()
        self.intro = Intro
        self.ki = 0

    def preloop(self):
        if self.ki == 0:
            self.intro = Intro
        else:
            self.intro = None

    # HELP
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

    def do_init(self, argv=None):
        # from importlib import reload
        # todo: Warning
        printX(f'[!] run init will flush all Global Config (Default in FileConfig)')
        printX(f'[+] Init 初始化中')
        # for k in GLOBAL_CONFIG:
        #     del globals()[k]

    def do_show(self, argv):
        if len(argv) < 1:  # or args[0] not in SHOW_CONFIG
            printX("[i] show [all | gi | gti | msi | fi | alive] / Payloads(Pay)")
            return 0
        elif argv[0].islower() and argv[0] not in SHOW_CONFIG:
            printX(f"[?] do you mean '{argv[0][0].upper() + argv[0][1:]}' ? Try It")
            return 0

        if argv[0] == 'all':
            for k in globals().keys():
                if allow_show(k):
                    print(f"{k}: {globals()[k]}")
        elif argv[0] == 'gi':
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
        elif argv[0] == 'gti':
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
        elif argv[0] == 'msi':
            # todo : debug
            _sshurl = URL(MyHostSSH)
            _sqlurl = URL(MyHostSQL)
            print(f"""
            |------------------|---------------------------------------------------------------
            |   Name           |  Current Setting                                             |
            |------------------|---------------------------------------------------------------
            | SSH Info         | Port: {str(_sshurl.port)}, User: {_sshurl.username}, Pass: {_sshurl.password} 
            | MySQL Info       | Port: {str(_sqlurl.port)}, User: {_sqlurl.username}, Pass: {_sqlurl.password} 
            | Vulner Info      | #todo:
            |------------------|---------------------------------------------------------------
            """)
        elif argv[0] == 'fi':
            print(f"""
            |------------------|---------------------------------------------------------------|
            |   Name           |  Current Setting                                              |
            |------------------|---------------------------------------------------------------|
            | FLag Path        | '{FlagPath}'
            | Flag Regular     | '{FlagRegular}'
            | Flag Length      | {FlagLen}
            |------------------|---------------------------------------------------------------|
            """)
        elif argv[0] == 'alive':
            printX(f'[!] Last scan time was{ScanTime}\nPlease Decide whether to Re-SCAN based on the actual situation')
        elif allow_show(argv[0]) and argv[0] in globals().keys():
            print(f"{argv[0]}: {globals()[argv[0]]}")
        elif argv[0] in ''.join([_ for _ in globals().keys() if allow_show(_)]):
            for k in [_ for _ in globals().keys() if allow_show(_)]:
                if argv[0] in k:
                    print(f"{k}: {globals()[k]}")
        else:
            printX("[-] Not Find this variable")

    def do_set(self, argv):
        args = ' '.join(argv).split('=')
        argv = args[0].split() + [args[-1]]
        keys = globals().keys()

        if len(argv) < 3 or argv[0] not in ['global', '-g', 'add' '-a', 'g', 'a']:
            printX(f"[i] -g global, -a add, set -g xxx=xxx, set add Flags flagxx, (-,=)均可省略")
            return 0
        elif argv[0] not in ['add', '-a', 'a'] and argv[1] not in keys:
            printX(f"[!] Need at least two param Or Not Find {argv[1]}")
            printX(f"[i] you can set the following options\n")
            print([_ for _ in keys if allow_show(_)])
            # 提示设置变量 至少两个参数，并且只能设置非魔法变量且有大写字母的全局变量
            return 0

        if allow_show(argv[1]):
            globals()[argv[1]] = argv[2]
            printX(f"[!] {argv[1]} -> {argv[2]}")
            if argv[1] == 'Mode':
                printX(f'[!] Change Mode should do `restart`')
                sys.argv[1] = argv[2]
            return 0
        else:
            printX("[-] Not allow change, Read-Only Variable")

    def do_unset(self, argv):
        if not argv or argv[0] not in globals().keys():
            printX("[!] need at least a param")
            printX("[i] you can unset the following options\n")
            print([_ for _ in globals().keys() if allow_show(_)])
            # 提示设置变量 至少两个参数，并且只能设置非魔法变量且有大写字母的全局变量
            return 0

        if allow_show(argv[0]):
            globals()[argv[0]] = ''
        else:
            printX("[-] Not allow unset, Read-Only Variable")

    # Auxiliary
    def do_timedown(self, argv=None):
        try:
            GSTimestamp = int(time.mktime(time.strptime(GSTime, "%Y-%m-%d %H:%M:%S")))
            if game_start_remind(GSTimestamp, DFTime):
                round_count_remind(GSTimestamp, DFTime, RTime, RCount)
                return 0
        except Exception as e:
            printX(f"[-] {e.__class__.__name__} {e}")

    def do_timeoff(self, argv=None):
        pass
        # self.prompt = time.asctime().split()[3] + PROMPT

    def do_scan(self, argv=None):
        if not argv:
            printX("[i] scan [alive | ssh | sql | vul] [-a all | -i indict | (port)]")
            return 1
        argv.append(argv[1] if len(argv) > 2 else 'default')
        if not ScanTime[0] or argv[1] in ['-a', 'all']:
            target = EyHostExample
        else:
            target = EyHosts

        def _update_ey(result: dict.items):
            for Ey in globals()['EyHosts']:
                for k, v in result:
                    if Ey == k: globals()['EyHosts'][Ey].update(v)
            globals()['EyHosts'].update({_: v for _, v in result if _ not in globals()['EyHosts']})

        if argv[0] == 'alive':
            try:
                port = int(argv[-1])
            except (IndexError, ValueError):
                port = 8000
            result = scan_alive(target, TeamReplaceStr, port)
            _update_ey(result.items())
        elif argv[0] == 'ping':
            result = scan_ping(target, TeamReplaceStr)
            _update_ey(result.items())
        elif argv[0] == 'ssh':
            pass
        elif argv[0] == 'sql':
            pass
        elif argv[0] == 'vul':
            pass
        else:
            printX("[-] no this option")
        return 0

    # Attack
    def do_shellin(self, argv=None):
        globals()['EyHosts'] = backdoor_in(EyHosts, MyHost)

    def do_getflag(self, argv=None):
        try:
            get_flag(EyHosts)
        except KeyboardInterrupt:
            print('\r', end='')
            printX("[!] Quit getflag")
        except Exception as e:
            printX(f"[-] {e.__class__.__name__} {e}")
        else:
            for flag in Flags:
                print(flag)

    def do_submit(self, argv=None):
        if not argv:
            print("submit [auto|manual flag{x}?]")
            return 0
        from modules.Attack import Flags
        if argv[0] == 'auto':
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

        elif argv[0] == '-m' and len(argv) > 1:
            for flag in argv[1:]:
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

    # Defense
    def do_checkme(self, argv=None):
        if not argv:
            status = check_me(MyHost, AliveStr)
            for host in EyHosts:
                if MyHost in host:
                    EyHosts[host] = status.split('m')[1].split('\x1b')[0]
            if 'Alive' in status:
                printX(f'[+] Myself Server is {status}, 200')
            else:
                printX(f'[!] Myself Server is {status}')
        else:
            add_monitor(MyHostSSH, argv[0])

    def do_getbackup(self, argv=None):
        if not argv:
            printX('[-] no path to save backup')
            return 0
        save_path = argv[0]
        if os.path.isdir(save_path):
            get_backup(MyHostSSH, save_path)
        else:
            printX(f'[-] no such directory: {save_path}')

    def do_mysql(self, argv=None):
        conn = connect_mysql(MyHostSQL)
        if conn is None:
            printX('[-] Failed to Connect My SQL')
            return 0
        sqlhelpcmd = [
            'show global variables like "general%";',
            'show global variables like "secure%";',
            "create user 'username'@'localhost' identified by 'password';",
            "set password for username=password('1234');",
            'flush privileges;',
        ]
        sqlcmd = '__'
        while sqlcmd not in 'exit_quit':
            try:
                sqlcmd = input("mysql>").strip()
                if sqlcmd[0:4] == 'help':
                    if sqlcmd[-1].isdigit() and 0 < int(sqlcmd[-1]) < 5:
                        sqlcmd = sqlhelpcmd[int(sqlcmd[-1])]
                    else:
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

    def do_clear(self, argv=None):
        clear()

    # todo : Test
    def do_test(self, argv=None):
        # connect_pwn('x')
        pass
        # todo: 1 AddCheckAliveStr

    # Persistence
    def do_upgrade(self, argv=None):
        # todo: dev git
        try:
            if os.access(f'{FRAME_DIR}/.git', os.R_OK):
                os.system('git pull')
        except Exception as e:
            printX(f"[-] {e.__class__.__name__}: {e}")

    def do_save(self, argv=None):
        # todo: dev sqlite3
        pass

    def do_restart(self, argv=None):
        # self.do_save()
        os.execv(sys.executable, ['python'] + sys.argv)

    def do_exit(self, argv=None):
        # todo : write in file
        # self.do_save()
        printX("[+] \n exit")
        exit(0)


if __name__ == '__main__':
    clear()
    console = AwdConsole()
    while True:
        try:
            console.cmdloop()
        except (KeyboardInterrupt, EOFError):
            console.ki = 1
            printX("[+] Interrupt: use the 'exit' command to quit", logtime=False)
        except Exception as e:
            printX(f"[-] {e.__class__.__name__} {e}")
            exit(1)
