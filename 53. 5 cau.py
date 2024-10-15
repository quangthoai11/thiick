# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:05:18 2024

@author: Admin
"""

def ham1(n):
    return sum(i for i in range(1, n + 1))

def ham2(n):
    return sum(i**2 for i in range(1, n + 1))

def ham3(n):
    return sum(1/i for i in range(1, n + 1))

def ham4(n):
    tong = 0
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua *= i
        tong += giai_thua
    return tong

def ham5(n):
    tich = 1
    for i in range(2, n+1):
        tich *= i
    return tich
        
if __name__=="__main__":
    n = int(input("Nhập một số nguyên dương n: "))
    print("Tổng S = 1 + 2 + ... + n:", ham1(n))
    print("Tổng S = 1^2 + 2^2 + ... + n^2:", ham2(n))
    print("Tổng S = 1 + 1/2 + 1/3 + ... + 1/n:", ham3(n))
    print("Tổng S = 1! + 2! + ... + n!:", ham4(n))
    print("Tích S = 1 * 2 * ... * n:", ham5(n))