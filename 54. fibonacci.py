# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:05:20 2024

@author: Admin
"""

def fibonacci(n):
    ds_fib = []
    a, b = 0, 1
    for i in range(n):
        ds_fib.append(a)
        a, b = b, a + b
    return ds_fib
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
print(f"Dãy Fibonacci với {n} phần tử: {fibonacci(n)}")