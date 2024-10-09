#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一张图解读Python3的基础语法(这是单行注释，用#号)

import os  # 导入模块

'''
这是多行注释，用三个单引号（或双引号）
'''


def main():
    print("Hello, Python3!")  # print向控制台输出信息。Python3中，print是一个函数，而不是一个语句。Python中通过缩进来表示代码块的范围，一般4个空格的缩进表示一个层级。
    print('=' * 10)  # 输出10个等号

    n = input('你叫什么名字？\n')  # input从控制台读取用户输入。'\n'表示换行
    print('你好，%s' % n)  # %s表示字符串格式化，%d表示整数格式化，%f表示浮点数格式化
    print('=' * 10)  # 字符串乘法表示重复输出字符串
    print('1.简单')
    print('2.普通')
    print('3.困难')
    lv = input('请选择级别：')
    x = func(n, int(lv))  # 函数调用，提供参数，并将返回值赋值给变量，func函数有两个参数，第一个参数是n，第二个参数是int(lv)，int(lv)表示将lv转换为整数类型，不规范的输入会导致报错。
    y = x + 1  # 变量必须先赋值才能使用
    y += 10  # 变量自增，相当于y = y + 10
    print('score is %s' % y)  # %s表示字符串格式化，%d表示整数格式化，%f表示浮点数格式化
    print('=' * 10)
    print('当前目录', os.getcwd())  # 函数嵌套调用，先调用os模块，再调用os模块中的getcwd函数。os.getcwd()获取当前目录，返回值作为print的参数打印。

    food = ['apple', 'orange', 'banana', 'cherry']  # []构造列表，可以存储多个值
    for f in food:  # for循环，遍历列表中的每个元素，需要定义循环变量，f表示当前遍历到的元素，结尾要有冒号，循环体内代码需要缩进
        print('我想吃' + f)  # 循环变量f江北一次赋值为food列表中的每个元素。字符串拼接，+号表示字符串连接。

    for i in range(10):  # range函数生成一个整数序列，为可迭代对象，从0开始，到10结束，不包含10。
        print(i, end=',')  # end参数表示print函数输出的结尾字符，默认是换行符，这里设置为逗号，表示输出时不换行，而是逗号分隔。
    print('main结束')


def func(name, level=1):  # 函数定义，函数名是func，参数是name和level，level为关键词参数，默认值1
    print("I'm", name)  # 双引号表示的字符串中可以包含单引号，单引号表示的字符串中可以包含双引号
    print('{} is level {}'.format(name, level))  # format函数，用于字符串格式化，{}表示占位符，format函数的参数会依次替换占位符
    c = len(name)  # 调用内置函数len()计算字符串长度
    s = name.find('s')  # 调用字符串的find方法，查找字符串中第一个出现的's'字符，返回索引值，如果找不到，返回-1
    if level < 1:  # if语句，判断条件，条件为False时，执行else语句块
        score = 0
    elif level > 1 and (c > 1 or s > 1):  # 逻辑运算符，and表示与，or表示或，not表示非
        score = 100
    else:
        score = 60
    return score  # 函数返回值，return语句后面的值作为函数的返回值，如果没有return语句，函数返回None


if __name__ == '__main__':  # 判断当前模块是被直接调用还是被其他文件导入，如果是主程序，则执行main函数
    main()
