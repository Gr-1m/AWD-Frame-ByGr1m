#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : Auxiliary.py
@Author     : Gr%1m
@Date       : 10/11/2023 9:42 pm
"""
import time


def game_start_remind(GSTimestamp, DFTime):
    remind_count = 0
    ATTimestamp = GSTimestamp + DFTime
    while remind_count < 1000:
        try:
            now = int(time.time())
            if now > ATTimestamp + 200:
                print(f"\r")
                return True
            if now > ATTimestamp:
                print(f"\r加固时间到，请开始比赛!!")
                return True
            elif now > GSTimestamp:
                print(f"\r比赛开始，加固时间还有{ATTimestamp - now}秒 !!", end='')
            else:
                print(f"\r\x1b[01;30;31m距比赛开始还剩{GSTimestamp - now}秒\x1b[0m", end='')
            time.sleep(1)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break

    return False


def round_count_remind(GSTimestamp, DFTime, RTime, RCount):
    count = RCount
    ATTimestamp = GSTimestamp + DFTime
    if int(time.time()) < GSTimestamp:
        print("The Competition hasn't started yet")
    while count > -1:
        try:
            now = int(time.time())
            nowRound = (now - ATTimestamp) // RTime + 1
            mods = (ATTimestamp - now) % RTime
            count = RCount - nowRound
            time.sleep(1)
        except KeyboardInterrupt:
            print('\n Quit Time Remind')
            break
        else:
            print(f"\rNow:第{nowRound}/{RCount}回合,还有{mods}秒", end='')
    else:
        print("\rThe Competition has Ended !")


# todo : time remind enable
if __name__ == '__main__':
    import os

    os.path.join('../../')
    from AWD_Frame_ByGr1m.Configs.edit_config import *

    GSTimestamp = int(time.mktime(time.strptime(GSTime, "%Y-%m-%d %H:%M:%S")))
    if game_start_remind(GSTimestamp, DFTime):
        round_count_remind(GSTimestamp, DFTime, RTime, RCount)
