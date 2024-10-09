#！/usr/bin/env python
# -*- coding: utf-8 -*-
def multiply_list(lst, factor):
    result = []  # 创建一个空列表，存储返回值
    for index, i in enumerate(lst):  # enumerate()函数返回可迭代的索引和值
        i *= factor  # 原列表中的值自乘系数
        result.append(i)
        # lst[index] = i  # 另一种方案：修改后的值添加到result列表中
    # return lst  # 另一种方案：返回修改后的列表
    return result  # 返回result列表

my_lst = [10, 11, 12]
lst_re = multiply_list(my_lst, 10)  # 返回列表赋值给lst_re
print(lst_re)  # 打印新列表


# 改进1，直接修改原列表
def multiply_list(lst, factor):  # 定义函数，参数为列表和系数
    for i in range(len(lst)):  # 遍历列表
        lst[i] *= factor  # 原列表中的值自乘系数
    return lst  # 返回修改后的列表


my_lst = [10, 11, 12]
multiply_list(my_lst, 10)
print(my_lst)  # 打印修改后的列表


# 改进2，使用列表解析
def multiply_list(lst, factor):  # 定义函数，参数为列表和系数
    return [i * factor for i in lst]  # 列表解析，返回一个新的列表


my_lst = [10, 11, 12]
lst_re = multiply_list(my_lst, 10)
print(lst_re)  # 打印新列表
