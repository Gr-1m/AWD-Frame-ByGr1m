#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : EnemyHost.py
@Author     : Gr%1m
@Date       : 11/11/2023 11:37 pm
"""


class EnemyHost:
    def __init__(self):
        self.enemy_host = ''
        self.enemy_index = 0
        self.status()

    def status(self):
        self.ssh = 'close'
        self.mysql = 'close'
