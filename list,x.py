# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:02:03 2024

@author: Admin
"""

def tim_phan_tu_list_x(list, x):
    if x in list:
        return list.index(x)
    else:
        return None
if __name__ == "__main__":
    list = [1, 3, 5, 7, 9, 11]
    x = [5, 10]
    for gia_tri in x:
        vi_tri = tim_phan_tu_list_x(list, gia_tri)
        if vi_tri is not None:
            print(f"Giá trị {gia_tri} có vị trí là {vi_tri}")
        else:
            print(f"Giá trị {gia_tri} có vị trí là None")