#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *


def solve_system(c, b):
    a = c[-3]
    a2 = c[-4]
    d = c[-2]
    a3 = -1 * b[-1]
    f = -1 * b[-2]
    ds = ((a ** 2 - d * a2) / (a * f - d * a3))
    dr = (a3 - a2 * ds) / a
    return dr, ds

def division_sintetica(pol, b, r, s):
    b[0] = pol[0]
    b[1] = pol[1] + r * b[0]
    for i, elemento in enumerate(pol[2:]):
        b[i+2] = elemento + r * b[i+1] + S * b[i]
    return b

def bairstow(pol, r, s, e):
    b = division_sintetica(pol,[None for x in range(len(pol))], r, s)
    while b[-1] > e and b[-2] > e:
        c = division_sintetica(b, [None for x in range(len(pol))], r, s)
        dr, ds = solve_system(c, b)
        r = r + dr
        s = s + ds
        b = division_sintetica(pol,[None for x in range(len(pol))], r, s)
    return r, s
    

def main():
	
	return 0

if __name__ == '__main__':
	main()
