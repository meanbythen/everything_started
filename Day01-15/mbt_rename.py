#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
# @Time  : 2020/5/26 14:47
# @Author: meanbythen

import os
from datetime import datetime
import random
import string

# oldnames = os.listdir(r'./mbt')
# newnames = [f'{name}.txt' for name in range(1, len(oldnames) + 1)]
# for oldname, newname in zip(oldnames, newnames):
#     oldname = r'./mbt/' + oldname
#     newname = r'./mbt/' + newname
#     if os.path.exists(newname):
#         print('文件已存在')
#     else:
#         os.rename(oldname, newname)  # os.renames(oldname, newname)参数需要带路径，否则会报错：FileNotFoundError: [WinError 2] 系统找不到指定的文件。
#


# 命名规则

# def rename_files(folder_path, prefix, type='txt'):
#     def name_format(prefix, seq, type):
#         return [f'{folder_path}//{prefix}{count}.{type}' for count in range(1, seq + 1)]
#
#     oldnames = [f'{folder_path}//{name}' for name in os.listdir(folder_path)]
#     newnames = name_format(prefix, len(oldnames), type)
#     for oldname, newname in zip(oldnames, newnames):
#         if os.path.exists(newname):
#             print('文件已存在')
#         else:
#             os.rename(oldname, newname)
#
#
# if __name__ == '__main__':
#     rename_files(r'./mbt', 'mbt', 'txt')

# def rename_files(folder_path, type='txt'):
#     def name_rule(prefix, type):
#         return [f'{folder_path}/{prefix}{middle}.{type}' for middle in os.listdir(folder_path)]
#
#     oldnames = [f'{folder_path}/{name}' for name in os.listdir(folder_path)]
#     newnames = name_rule(datetime.now().strftime('%Y%m%d'), type)
#     for oldname, newname in zip(oldnames, newnames):
#         if os.path.exists(newname):
#             print('文件已存在')
#         else:
#             os.rename(oldname, newname)
#
#
# if __name__ == '__main__':
#     rename_files(r'./mbt', 'doc')


sn = 1


def rename_rule(oldname, num):
    match num:
        case '1':
            global sn
            sn += 1
            return f'{str(sn)}.{oldname.split(".")[-1]}'
        case '2':
            return f'{datetime.now().strftime('%Y%m%d')}.{oldname.split(".")[-1]}'
        case '3':
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16)) + '.' + oldname.split(".")[-1]


def filter_rule(filename, file_type):
    return filename.endswith(file_type)


def error_handle():
    pass


def rename_files(folder_path, num, filter=None, handle=None):
    oldnames = [f'{folder_path}/{name}' for name in os.listdir(folder_path)]
    for oldname in oldnames:
        print('老名字', oldname)
        if filter and filter_rule(oldname, filter):
            newname = f'{folder_path}/' + rename_rule(oldname, num)
            if os.path.exists(newname):
                print('文件已存在')
            else:
                os.rename(oldname, newname)
        else:
            newname = f'{folder_path}/' + rename_rule(oldname, num)
            print("新名字", newname)
            if os.path.exists(newname):
                print('文件已存在')
            else:
                os.rename(oldname, newname)


if __name__ == '__main__':
    folder_path = r'./mbt'
    rename_files(folder_path, '3')
