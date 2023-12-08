#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Auxiliary.py
@Author     : Gr%1m
@Date       : 10/11/2023 9:42 pm
"""
import os as _os
from time import sleep, localtime, strftime, time as _time

import requests
import subprocess

from func.CmdColors import printX, progress_bar

FLUSH_LINE = "\x1b[K"
ScanTime = ['']
_Now = lambda x=None: int(_time())
alive_first = lambda x: printX('[!] Please scan alive/ping first') if type(x) == str or not x else True


def game_start_remind(GSTimestamp, DFTime):
    remind_count = 0
    ATTimestamp = GSTimestamp + DFTime
    # print('\x1b[2F', end='')
    while remind_count < 1000:
        try:
            now = _Now()
            if now > ATTimestamp + 200:
                print(f"\r", end='')
                return True
            if now > ATTimestamp:
                print(f"\r加固时间到，请开始比赛!!", end=FLUSH_LINE + '\n')
                return True
            elif now > GSTimestamp:
                print(f"\r比赛开始，加固时间还有{ATTimestamp - now}秒 !!", end=FLUSH_LINE)
            else:
                print(f"\r\x1b[01;30;31m距比赛开始还剩{GSTimestamp - now}秒\x1b[0m", end=FLUSH_LINE)
            sleep(1)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break

    return False


def round_count_remind(GSTimestamp, DFTime, RTime, RCount):
    count = RCount
    ATTimestamp = GSTimestamp + DFTime
    if _Now() < GSTimestamp:
        print("The Competition hasn't started yet")
    while count > -1:
        try:
            now = _Now()
            nowRound = (now - ATTimestamp) // RTime + 1
            mods = (ATTimestamp - now) % RTime
            count = RCount - nowRound
            print(f"\rNow:第{nowRound}/{RCount}回合,还有{mods}秒", end=FLUSH_LINE)
            sleep(0.2)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break
    else:
        print("\rThe Competition has Ended !")


# scan_alive, scan_ping Eyhosts初始为代替字符,扫描后为字典,判断是否为字典,选择新增或更新
# 其他扫描需要先scan alive或ping,将敌人靶机变量更新为字典再开始扫描

def scan_alive(ey_hosts, replace_str: str, port: int):
    results = []
    ScanTime[0] = strftime("%Y-%m-%d %H:%M:%S", localtime(_time()))
    if not alive_first(ey_hosts):
        for i in range(1, 255):
            url = f"http://{ey_hosts.replace(replace_str, str(i))}:{port}/"
            print(f'\r\x1b[01;30;34m[+]\t\t\t {progress_bar(i, 255)}\x1b[0m', end=FLUSH_LINE)
            try:
                res = requests.get(url, timeout=(0.01, 1))
                print(f'\r\x1b[01;30;34m[+] "{url}", # {res.status_code} {FLUSH_LINE}')
                results.append(f'{ey_hosts.replace(replace_str, str(i))}')
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
            except Exception:
                pass
        print('\x1b[0m')
        if not results:
            return {}
        return dict.fromkeys(results, {port: 'Alive'})
    elif type(ey_hosts) == dict:
        for ey in ey_hosts:
            url = f"http://{ey}:{port}/"
            try:
                res = requests.get(url, timeout=(1, 1))
                print(f'\x1b[01;30;34m[+] "{url}", # {res.status_code} \x1b[0m{FLUSH_LINE}')
                if res.status_code != 200:
                    ey_hosts[ey].update({port: 'Down'})
                else:
                    ey_hosts[ey].update({port: 'Alive'})
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
                break
            except Exception:
                print('\x1b[0m', end='')
        return ey_hosts


def scan_ping(ey_hosts, replace_str):
    if _os.name == 'nt':
        _ping = f'ping -n 1 '
    else:
        _ping = f'ping -c 1 '

    ScanTime[0] = strftime("%Y-%m-%d %H:%M:%S", localtime(_time()))
    if not alive_first(ey_hosts):
        results = []
        for i in range(255):
            try:
                ping_cmd = _ping + ey_hosts.replace(replace_str, str(i))
                print(f'\r\x1b[01;30;34m[+]\t\t\t {progress_bar(i, 255)}\x1b[0m', end=FLUSH_LINE)
                responce = subprocess.run(ping_cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                          timeout=0.04)
                responce = responce.returncode
            except subprocess.TimeoutExpired:
                responce = 999
            except KeyboardInterrupt:
                responce = -1
                printX("[-] Quit Scan Alive")

            if responce == 0:
                results.append(ey_hosts.replace(replace_str, str(i)))
        print('\x1b[0m')
        if not results:
            return ey_hosts
        return dict.fromkeys(results, {'ping': 'Alive'})
    elif type(ey_hosts) == dict:
        for ey in ey_hosts:
            try:
                ping_cmd = _ping + ey
                printX(f'[+] {ping_cmd}')
                responce = subprocess.run(ping_cmd.split(), stdout=subprocess.DEVNULL, timeout=0.2)
                responce = responce.returncode
            except subprocess.TimeoutExpired:
                responce = 999
            except KeyboardInterrupt:
                responce = -1
                printX("[-] Quit Scan Alive")

            if responce != 0:
                ey_hosts[ey].update({'ping': 'Down'})
            else:
                ey_hosts[ey].update({'ping': 'Alive'})
        return ey_hosts


def scan_ssh(ey_hosts, myhostssh):
    if not alive_first(ey_hosts):
        return 0
    for ey in ey_hosts:
        pass


def scan_vul(ey_hosts):
    if not alive_first(ey_hosts):
        return 0


def http_confusion(eyhosts, count=1):
    # 敌人主机变量为字典时,可以进行http流量混淆,发送大量疑似后门连接的流量 触发报警
    if not alive_first:
        return 0
    bdfile = {'shell.php', 'x.php', '1ndex.php', 'yjh.php', '1.php'}
    payload = {'cat /flag', 'rm -f', 'whoami'}
    while count != 0:
        for ey in eyhosts:
            for bdf in bdfile:
                url = f'http://{ey}/{bdf}'
                for iii in payload:
                    try:
                        data = {'payload': iii}
                        requests.post(url, data=data, timeout=(0.01, 0.01))
                        printX(f'[+] ')
                    except KeyboardInterrupt:
                        return 0
                    except Exception:
                        pass
        count -= 1


# todo : time remind enable
# if __name__ == '__main__':
#     import os
#
#     os.path.join('../../')
#     from AWD_Frame_ByGr1m.Configs.edit_config import *
#
#     GSTimestamp = int(time.mktime(time.strptime(GSTime, "%Y-%m-%d %H:%M:%S")))
#     if game_start_remind(GSTimestamp, DFTime):
#         round_count_remind(GSTimestamp, DFTime, RTime, RCount)
# x = {'k1': {'v1': 'xx1', 'v2': 'xx2'}}
# xx = {'k1': {'v1': 'xxxx'}}
