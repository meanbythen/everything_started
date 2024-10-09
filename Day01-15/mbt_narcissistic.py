#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def bit(num):
#     return (num//100, num//10%10, num%10)
#
# def is_narcissistic(num):
#     return num == sum([i**3 for i in bit(num)])
#
# if __name__ == '__main__':
#     nar = []
#     for i in range(100, 1000):
#         if is_narcissistic(i):
#             nar.append(i)
#     print(nar)

nar = []
for i in range(100, 1000):
    if i == sum(int(j)**3 for j in str(i)):
        nar.append(i)

print(nar)
