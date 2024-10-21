# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:03:44 2024

@author: Admin
"""

import random
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    so_nguyen = random.randint(-99, 98)
    if is_prime(so_nguyen):
        print(f"Số {so_nguyen} là số nguyên tố.")
    else:
        print(f"Số {so_nguyen} không phải là số nguyên tố.")