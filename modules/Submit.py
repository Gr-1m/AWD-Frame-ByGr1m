#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Submit.py
@Author     : Gr%1m
@Date       : 13/11/2023 10:36 pm
"""
import requests


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


# def getflag(ey_hosts, payloads):
#     flags = []
#     for target in ey_hosts:
#         get_flag = requests.get(f"http://{target}{payloads}")
#         getext = get_flag.text
#         if 'flag{' in getext:
#             flags.append('flag' + getext.split('flag{')[0].split('}')[0] + '}')
#             print(f'{target} is vul able')
#     return flags
