#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : scan_ey.py
@Author     : Gr%1m
@Date       : 11/11/2023 6:38 pm
"""
from config import *
import requests

# About Game Info

for i in range(1, 255):
    url = f"http://{EyHosts.replace(TeamReplaceStr, str(i))}"
    try:
        if url != f"http://{MyHost}":
            html = requests.get(url, timeout=2)
            print(f'"{url}",')
    except Exception:
        pass

"""
http://192-168-1-13.pvp3459.bugku.cn
http://192-168-1-21.pvp3459.bugku.cn
http://192-168-1-98.pvp3459.bugku.cn
http://192-168-1-103.pvp3459.bugku.cn
http://192-168-1-237.pvp3459.bugku.cn
http://192-168-1-246.pvp3459.bugku.cn
http://192-168-1-247.pvp3459.bugku.cn

98 103 237 246 247
set password for cms=password('imMYSQL@admin');
set password for cms=password('eb0d39d2931c480f');
"""
