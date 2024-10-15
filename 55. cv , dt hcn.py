# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:05:23 2024

@author: Admin
"""

def kiemtra(n):
    if n < 0 and n % 2 != 0:
        return -1
    elif n > 0 and n % 2 == 0:
        return 1
    return 0
n = int(input("Nhập một số: "))
print(kiemtra(n))