#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def max_number(lst):  # 寻找列表lst的最大值
    mx = -float('inf') # 初始化最大值为负无穷
    for i in lst:
        if i > mx:
            mx = i
    return mx


print(max_number([3, 1, 2]))  # 自行“测试调试”确保算法的准确性
