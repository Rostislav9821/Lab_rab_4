#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Введите x: "))
    if x == 0:
        print("x - не может быть равен 0", file=sys.stderr)
        exit(1)

    a = x
    S, n = a, 0

    while math.fabs(a) > EPS:
        a *= (- x * (2 * n + 1)) / ((2 * n + 3) * (n + 1))
        S += a
        n += 1

    print(f"Chi{x} = {2 / math.sqrt(math.pi) *  S}")