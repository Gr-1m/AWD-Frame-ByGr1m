#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : TimeRemind.py
@Author     : Gr%1m
@Date       : 10/11/2023 9:42 pm
"""
from config import *
import time

GSTimestamp = int(time.mktime(time.strptime(GSTime, "%Y-%m-%d %H:%M:%S")))
ATTimestamp = GSTimestamp + DFTime


def game_start_remind():
    remind_count = 0
    while remind_count < 1000:
        try:
            now = int(time.time())
            if now > ATTimestamp:
                print(f"\r加固时间到，请开始比赛!!")
                return True
            elif now > GSTimestamp:
                print(f"\r比赛开始，加固时间还有{ATTimestamp - now}秒 !!", end='')
            else:
                print(f"\r\x1b[01;30;31m距下班还剩{GSTimestamp - now}秒\x1b[0m", end='')
            time.sleep(1)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break

    return False


def round_count_remind():
    count = RCount
    if int(time.time()) < GSTimestamp:
        print("The Competition hasn't started yet")
    while count > 0:
        try:
            now = int(time.time())
            nowRound = (now - ATTimestamp) // RTime + 1
            mods = (ATTimestamp - now) % RTime
            count = nowRound
            print(f"\rNow:第{nowRound}/{RCount}回合,还有{mods}秒", end='')
            time.sleep(1)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break


if game_start_remind():
    round_count_remind()
