#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import exp, fabs

def f(x):
    return exp(x)-(x)**2+4

def biseccion(a,b,e):
    alfa = a + (b-a)/2.0
    if fabs(f(alfa)) < e and (a+b)/2.0 < e:
        return alfa
    else:
        if f(a)*f(alfa) < 0:
            return biseccion(a,alfa,e)
        else:
            return biseccion(alfa,b,e)



def main():
	
    a = raw_input('ingrese a: ')
    b = raw_input('ingrese b: ')
    e = raw_input('ingrese e: ')
    print biseccion(float(a),float(b),float(e))

if __name__ == '__main__':
	main()
