#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : customGr1m
@file       : CmdColors.py
@Author     : Gr%1m
@Date       : 10/11/2023 4:35 pm
"""
# -*- coding:utf-8 -*-#
import time


class bcolor(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# green
def printGreen(mess, show=True):
    if show:
        print(bcolor.OKGREEN + mess + bcolor.ENDC)
    return bcolor.OKGREEN + mess + bcolor.ENDC


# red
def printRed(mess, show=True):
    if show:
        print(bcolor.FAIL + mess + bcolor.ENDC)
    return bcolor.FAIL + mess + bcolor.ENDC


# yellow
def printYellow(mess, show=True):
    if show:
        print(bcolor.WARNING + mess + bcolor.ENDC)
    return bcolor.WARNING + mess + bcolor.ENDC


def printX(context, *args, **kwargs) -> None:
    logtime = True
    try:
        if context[0] == '[' and context[2] == ']':
            prompt = context[1].lower()
            main_text = context[3:].lstrip()
            if prompt == '0':
                context = '\x1b[01;30;30m[0]\x1b[0m ' + main_text
            elif prompt == '-':
                context = '\x1b[01;30;31m[-]\x1b[0m ' + main_text
            elif prompt.lower() == 'i':
                logtime = False
                context = '\x1b[01;30;32m[i]\x1b[0m ' + main_text
            elif prompt.lower() == 'w' or prompt.lower() == '!':
                logtime = False
                context = '\x1b[01;30;33m[W]\x1b[0m ' + main_text
            elif prompt == '+':
                context = '\x1b[01;30;34m[+]\x1b[0m ' + main_text
            elif prompt == '*':
                context = '\x1b[01;30;35m[*]\x1b[0m ' + main_text
            elif prompt.upper() == 'F':
                context = '\x1b[01;30;36m[F]\x1b[0m ' + main_text
            else:
                logtime = False
                context = '\x1b[01;30;37m[!]\x1b[0m ' + main_text
        else:
            context = '\x1b[01;30;38m[?]\x1b[0m ' + context.lstrip()
    except IndexError:
        context = '\x1b[01;30;37m[E]\x1b[0m ' + f"Log Input Error:{context.lstrip()}"

    finally:
        if logtime:
            print(f"[\x1b[01;30;32m{time.asctime().split()[3]}\x1b[0m] {context}", *args, **kwargs)
        else:
            print(f"{context}", *args, **kwargs)
        return None

# todo: this is a file about Terminal beautification function
#   The class bcolor can be & should be Optimized, and the function printX too.
