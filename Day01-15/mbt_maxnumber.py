#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def max_number(lst):
    max_num = lst[0]
    try:
        for i in lst:
            if i > max_num:
                max_num = i
    except TypeError:
        print("列表存在非数字元素")
    else:
        return max_num


lst = ["a", 2, 3, 4, 5, 6, 7, 8, 9]
print(max_number(lst))
