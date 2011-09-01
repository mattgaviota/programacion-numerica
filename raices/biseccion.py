#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import exp, fabs

def f(x):
    return (x)**3-(x)-1

def biseccion(a,b,e):
    alfa = a + (b-a)/2.0
    while fabs(f(alfa)) > e and (b-a)/2.0 > e:
        if f(a)*f(alfa) < 0:
            b = alfa
        else:
            a = alfa
        alfa = a + (b-a)/2.0
    return alfa

def regula_falsi(a,b,e):
    alfa = (a * f(b) - b * f(a))/ (f(b) - f(a))
    while fabs(f(alfa)) > e and (b-a)/2.0 > e:
        if f(a)*f(alfa) < 0:
            b = alfa
        else:
            a = alfa
        alfa = ((a * f(b)) - ( b * f(a)))/ (f(b) - f(a))
    return alfa

def secante(a,b,e):
    alfa = b - (f(b) * ((b - a) / (f(b) - f(a))))
    while fabs(f(alfa)) > e:
        a = b
        b = alfa
        alfa = ((a * f(b)) - ( b * f(a)))/ (f(b) - f(a))
    return alfa
    
def main():
	
    a = raw_input('ingrese a: ')
    b = raw_input('ingrese b: ')
    e = raw_input('ingrese e: ')
    print 'biseccion :', biseccion(float(a),float(b),float(e))
    print 'regula falsi : ', regula_falsi(float(a), float(b), float(e))
    print 'secante : ', secante(float(a), float(b), float(e))
    
if __name__ == '__main__':
	main()
