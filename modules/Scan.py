#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Scan.py
@Author     : Gr%1m
@Date       : 13/11/2023 10:35 am
"""
from func.CmdColors import printX
from time import time, localtime, strftime
import requests

ScanTime = ''


# About Game Info
def scan_alive(ey_hosts, my_host: str, replace_str: str):
    results = []
    ScanTime = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
    if type(ey_hosts) == str:
        for i in range(1, 255):
            url = f"http://{ey_hosts.replace(replace_str, str(i))}"
            print(f'\r\x1b[01;30;34m[+]\t\t\t {round(i * 100 / 255)}% [', '>' * round(i * 100 / 255), end='')
            try:
                res = requests.get(url, timeout=(0.01, 1))
                print(f'\r\x1b[01;30;34m[+] "{url}", # {res.status_code}', ' ' * 100)
                results.append(f'{ey_hosts.replace(replace_str, str(i))}')
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
                return dict.fromkeys(results, 'Alive')
            except Exception:
                print('\x1b[0m', end='')
                continue
        print('\x1b[0m\n', end='')
        return dict.fromkeys(results, 'Alive')
    elif type(ey_hosts) == dict:
        for ey in ey_hosts:
            url = f"http://{ey}/"
            try:
                res = requests.get(url, timeout=(1, 1))
                print('\x1b[01;30;34m[+]', end='')
                print(f'"{url}", # {res.status_code}')
                print('\x1b[0m', end='')
                if res.status_code != 200:
                    ey_hosts[ey] = '\x1b[01;31mDown\x1b[0m'
            except KeyboardInterrupt:
                printX("[-] Quit Scan Alive")
                break
            except Exception:

                print('\x1b[0m', end='')
        return ey_hosts


def scan_vul(ey_hosts):
    pass
