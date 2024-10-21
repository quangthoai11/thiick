# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:02:39 2024

@author: Admin
"""

def kiem_tra_chuoi_palindrome(chuoi):
    chuoi = chuoi.replace(" ", "").lower()
    return chuoi == chuoi[::-1]
if __name__ == "__main__":
    chuoi1 = "hello"
    chuoi2 = "madam"
    if kiem_tra_chuoi_palindrome(chuoi1):
        print(f'"{chuoi1}" là chuỗi Palindrome.')
    else:
        print(f'"{chuoi1}" không phải là chuỗi Palindrome.')
    if kiem_tra_chuoi_palindrome(chuoi2):
        print(f'"{chuoi2}" là chuỗi Palindrome.')
    else:
        print(f'"{chuoi2}" không phải là chuỗi Palindrome.')