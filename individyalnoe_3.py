#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

n = int(input("Введите число n(от 1 до 4): "))
z1 = 1
z2 = 10
z3 = 100
z4 = 1000
a = 0
if __name__ == '__main__':
    if n == 1:
        while z1 < 10:
            a = a + z1
            z1 += 1
    if n == 2:
        while z2 < 100:
            a = a + z2
            z2 += 1
    if n == 3:
        while z3 < 1000:
            a = a + z3
            z3 += 1
    if n == 4:
        while z4 < 10000:
            a = a + z4
            z4 += 1
print(f"x = {a}")