# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:08:16 2025

@author: User
"""

import time

t1 = time.time()

def GetTime(fmt):
    lot = time.localtime(t1)
    st = time.strftime(fmt,lot)
    return st


if __name__ == '__main__':
    print(GetTime("%Y-%m-%d %H:%M:%S"))
    print(GetTime("%Y-%m-%d %H:%M:%S %a"))
    print(GetTime("%Y-%b-%d %H:%M:%S %a"))
    print(GetTime("%Y-%B-%d %H:%M:%S %A"))
