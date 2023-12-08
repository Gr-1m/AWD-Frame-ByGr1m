#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : AWD-Frame-ByGr1m
@file       : Persistence.py
@Author     : Gr%1m
@Date       : 7/12/2023 1:29 pm
"""
from Configs.frame_config import FRAME_DIR
import sqlite3

"""
eyHosts: # 对手的靶机
    主键 hostname
    ping    -> 0: Down   1: Alive   
    port80  -> 0: Down   1: Alive   2:Infected  3-10:Damaged->payload
    port xx -> 0: Down   1: Alive   2:Infected  3-10:Damaged->payload
    
payload:

vulners:

"""


class testData():
    def __init__(self):
        self.eyHosts = {'192.168.122.1': 'Alive'}


def execute_sql(sql):
    try:
        conn = sqlite3.connect(f"{FRAME_DIR}/data/Afdata.db")
    except:
        conn = sqlite3.connect(f"{FRAME_DIR}/data/Afdata.db")
    c = conn.cursor()

    try:
        result = c.execute(sql)
        conn.commit()
        # conn.close()
        return result
    except:
        return False


def init_sql():
    pass


def read_from_file():
    pass
