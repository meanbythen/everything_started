#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

"""
素数是指只能被1和自身整除的正整数。第一个素数是2，它还是唯一的偶数素数。除了2以外，所有的素数都是奇数。素数没有除了1和自身以外其他的因数，如果有其他因数，因数必定成对出现，一个小于平方根，一个大于平方根，所以对于大于2的正整数n，只需迭代2-√n间是否有n的因数即可。
"""
def is_prime(number):
    if number < 2:  # 小于2的数不是素数
        return False
    for i in range(2, int(math.sqrt(number)) + 1):  # 只需要判断到该数的平方根
        if number % i == 0:  # 如果能被整除，则不是素数
            return False  # 退出循环
    return True  # 如果2-自身平方根之间没有其他因数，则是素数


if __name__ == '__main__':
    while True:  # 循环读取用户输入
        number = int(input('请输入一个正整数:'))
        if is_prime(number):  # 调用函数判断是否为素数
            print(f'{number}是素数')
        else:
            print('{number}不是素数')
        if input('是否继续(y/n):') == 'n':  # 判断是否继续
            break  # 如果输入n，则退出循环
