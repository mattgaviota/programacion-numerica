#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import exp, fabs

def f(x):
    return exp(x) - x ** 2 + 4


def fp(x):
    return exp(x) - 2 * x


alfa_biseccion = []
a_biseccion = []
b_biseccion = []
f_alfa_biseccion = []

alfa_secante = []
a_secante = []
b_secante = []
f_alfa_secante = []

b_newton = []
alfa_newton = []
f_alfa_newton = []

def biseccion(a,b,e):
    alfa = a + (b-a)/2.0
    alfa_biseccion.append(alfa)
    a_biseccion.append(a)
    b_biseccion.append(b)
    while fabs(f(alfa)) > e and (b-a)/2.0 > e:
        f_alfa_biseccion.append(f(alfa))
        if f(a)*f(alfa) < 0:
            b = alfa
            b_biseccion.append(b)
        else:
            a = alfa
            a_biseccion.append(a)
        alfa = a + (b-a)/2.0
        alfa_biseccion.append(alfa)
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
    a_secante.append(a)
    b_secante.append(b)
    alfa_secante.append(alfa)
    while fabs(f(alfa)) > e:
        f_alfa_secante.append(f(alfa))
        a = b
        a_secante.append(a)
        b = alfa
        b_secante.append(b)
        alfa = ((a * f(b)) - ( b * f(a)))/ (f(b) - f(a))
        alfa_secante.append(alfa)
    return alfa


def newton(b, e):
    alfa = b - (f(b) / fp(b))
    alfa_newton.append(alfa)
    b_newton.append(b)
    while fabs(f(alfa)) > e:
        f_alfa_newton.append(f(alfa))
        b = alfa
        alfa = b - (f(b) / fp(b))
        b_newton.append(b)
        alfa_newton.append(alfa)
    return alfa


def show_biseccion():
    print 'a: '
    for index, element in enumerate(a_biseccion):
        print index, element
    print 'b: '
    for index, element in enumerate(b_biseccion):
        print index, element
    print 'alfa: '
    for index, element in enumerate(alfa_biseccion):
        print index, element
    print 'f de alfa: '
    for index, element in enumerate(f_alfa_biseccion):
        print index, element


def show_regula():
    pass


def show_secante():
    print 'a: '
    for index, element in enumerate(a_secante):
        print index, element
    print 'b: '
    for index, element in enumerate(b_secante):
        print index, element
    print 'alfa: '
    for index, element in enumerate(alfa_secante):
        print index, element
    print 'f de alfa: '
    for index, element in enumerate(f_alfa_secante):
        print index, element

def show_newton():
    print 'b: '
    for index, element in enumerate(b_newton):
        print index, element
    print 'alfa: '
    for index, element in enumerate(alfa_newton):
        print index, element
    print 'f de alfa: '
    for index, element in enumerate(f_alfa_newton):
        print index, element

def main():
	
    a = raw_input('ingrese a: ')
    b = raw_input('ingrese b: ')
    e = raw_input('ingrese e: ')
    print 'biseccion :', biseccion(float(a),float(b),float(e))
    show_biseccion()
    print 'regula falsi : ', regula_falsi(float(a), float(b), float(e))
    show_regula()
    print 'secante : ', secante(float(a), float(b), float(e))
    show_secante()
    print 'newton : ', newton(float(b), float(e))
    show_newton()

if __name__ == '__main__':
	main()
