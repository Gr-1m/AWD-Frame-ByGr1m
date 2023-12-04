#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Scan.py
@Author     : Gr%1m
@Date       : 13/11/2023 10:35 am
"""
from func.CmdColors import printX, progress_bar
from time import time, localtime, strftime
import requests, subprocess, os

ScanTime = ['']
alive_first = lambda x: printX('[!] Please scan alive/ping first') if type(x) == str or not x else True


# About Game Info
# scan_alive, scan_ping Eyhosts初始为代替字符,扫描后为字典,判断是否为字典,选择新增或更新
# 其他扫描需要先scan alive或ping,将敌人靶机变量更新为字典再开始扫描
def scan_alive(ey_hosts, my_host: str, replace_str: str, port: int):
    results = []
    ScanTime[0] = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    if not alive_first(ey_hosts):
        for i in range(1, 255):
            url = f"http://{ey_hosts.replace(replace_str, str(i))}:{port}/"
            print(f'\r\x1b[01;30;34m[+]\t\t\t {progress_bar(i, 255)}\x1b[0m\x1b[K', end='')
            try:
                res = requests.get(url, timeout=(0.01, 1))
                print(f'\r\x1b[01;30;34m[+] "{url}", # {res.status_code} \x1b[K')
                results.append(f'{ey_hosts.replace(replace_str, str(i))}')
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
            except Exception:
                pass
        print('\x1b[0m\n', end='')
        if not results:
            return ey_hosts
        return dict.fromkeys(results, {port: 'Alive'})
    elif type(ey_hosts) == dict:
        for ey in ey_hosts:
            url = f"http://{ey}:{port}/"
            try:
                res = requests.get(url, timeout=(1, 1))
                print(f'\x1b[01;30;34m[+] "{url}", # {res.status_code} \x1b[0m\x1b[K')
                if res.status_code != 200:
                    ey_hosts[ey].update({port: 'Down'})
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
                break
            except Exception:
                print('\x1b[0m', end='')
        return ey_hosts


def scan_ping(ey_hosts, replace_str):
    if os.name == 'nt':
        ping_cmd = f'ping -n 1 '
    else:
        ping_cmd = f'ping -c 1 '
    if not alive_first(ey_hosts):
        results = []
        for i in range(255):
            try:
                ping_cmd += ey_hosts.repalce(replace_str, str(i))
                print(f'\r\x1b[01;30;34m[+]\t\t\t {progress_bar(i, 255)}\x1b[0m\x1b[K', end='')
                responce = subprocess.run(ping_cmd.split(), timeout=1)
                responce = responce.returncode
            except subprocess.TimeoutExpired:
                responce = 999
            except KeyboardInterrupt:
                responce = -1
                printX("[-] Quit Scan Alive")

            if responce == 0:
                results.append(ey_hosts.repalce(replace_str, str(i)))
        if not results:
            return ey_hosts
        return dict.fromkeys(results, {'ping': 'Alive'})
    elif type(ey_hosts) == dict:
        for ey in ey_hosts:
            try:
                ping_cmd += ey
                responce = subprocess.run(ping_cmd.split(), timeout=1)
                responce = responce.returncode
            except subprocess.TimeoutExpired:
                responce = 999
            except KeyboardInterrupt:
                responce = -1
                printX("[-] Quit Scan Alive")
            if responce != 0:
                ey_hosts[ey].update({'ping': 'Down'})


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
