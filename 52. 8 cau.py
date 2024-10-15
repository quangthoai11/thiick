# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:05:16 2024

@author: Admin
"""

import math
#a
def can(n):
    return math.sqrt(n)
#b
def so_dao(n):
    return int(str(n)[::-1])
#c
def chinh_phuong(n):
    return math.isqrt(n) ** 2 == n
#d
def nguyen_to(n):
    return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
#e
def tich_le(n):
    tich = 1
    for i in str(n):
        if int(i) % 2:
            tich *= int(i)
    return tich if tich > 1 else 0
#f
def tong_nguyento(n):
    return sum(i for i in range(2, n) if nguyen_to(i))
#g
def tong_chinhphuong(n):
    return sum(i * i for i in range(1, int(math.sqrt(n)) + 1))
#h
def tong_uoc_duong(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

if __name__ == "__main__":
    n = int(input("Nhập một số nguyên dương n: "))
    
    print(f"Căn bậc 2 của {n}: {can(n)}")
    print(f"Số đảo của {n}: {so_dao(n)}")
    print(f"Số chính phương? {chinh_phuong(n)}")
    print(f"Số nguyên tố? {nguyen_to(n)}")
    print(f"Tích các chữ số lẻ: {tich_le(n)}")
    print(f"Tổng số nguyên tố < {n}: {tong_nguyento(n)}")
    print(f"Tổng số chính phương < {n}: {tong_chinhphuong(n)}")
    print(f"Tổng ước số dương của {n}: {tong_uoc_duong(n)}")