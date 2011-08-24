#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Libreria para convertir números entre distintas bases. Ademas para pasarlos
# a punto flotante y normalizarlos ya sea por corte o por simetría
#
# Autor: Matias Novoa

#TODO Hacer los docstrings 18 % 

import re


def descomponer_numero(numero):
    '''
        descomponer_numero(string) -> string
        
        Función que dado un número lo descompone en su parte real y decimal.
        Devuelve una tupla formada de la siguiente manera:
        
            (parte_entera, parte_decimal, signo)
            
        El signo es 0 si negativo o 1 si es positivo.
        Acepta , ó . como separador de decimal.
        
        descomponer_numero(numero)
        
        Ej:
            >> descomponer_numero('10.75')
            >> (10, 75, 1)
    '''
    if ',' in numero or '.' in numero:
        if numero[0] == '-':
            signo = 0
        else:
            signo = 1
        regex = r"([\dA-Fa-f]*)[,\.]([\dA-Fa-f]*)"
        flotante = re.search(regex, numero)
        if flotante:
            enteros = flotante.group(1)
            decimales = flotante.group(2)
            return (enteros, decimales, signo)
        else:
            return (None, None, None)
    else:
        if numero[0] == '-':
            return (numero[1:], '0', 0)
        else:
            return (numero, '0', 1)


def sumar_1(numero, base):
    '''
        sumar_1(string, string) -> string
        
        Función que suma 1(una) unidad a la parte decimal de un número(string)
        tomando en cuenta la base(string) en la que se encuentra el número.
        
        sumar_1(numero, base)
        
        Ej:
            >> sumar_1('147', '8')
            >> '150'
    '''
    if numero:
        if len(numero) >= 1:
            digito = int(a_base_10(numero[-1])) + 1
            if digito < int(base):
                return numero[:-1] + de_base_10(str(digito))
            else:
                return sumar_1(numero[:-1], base) + '0'
        else:
            return '1.'
    return '1.'

def redondear(numero, base, t):
    '''
        redondear(string, string, integer) -> string
        
        Redondea la parte decimal de un número, dado su base y una cantidad de
        digitos (t). Si el digito t+1 > base/2 le suma 1 al digito t
        
        redondear(numero, base, t)
        
        Ej:
            >> redondear('277', '8', 2)
            >> '30'
        
    '''
    if len(numero) > t:
        digito = int(a_base_10(numero[t]))
        numero_nuevo = numero[:t]
        base = int(base)
        if digito >= base/2:
            return sumar_1(numero_nuevo, base)            
        else:
            return ''
    else:
        return numero
        
def num_de_base(base):
    digitos = '0123456789ABCDEF'
    try:
        base = int(base)
    except:
        base = 0
    if 2 <= base <= 16:
        return digitos[:base]
    else:
        return ''

def verificar_base(numero, base):
    
    entera, decimal, signo = descomponer_numero(numero)
    digitos = entera + decimal
    digitos = digitos.upper()
    posibles_digitos = num_de_base(base)
    if posibles_digitos:
        res = 0
        for digito in digitos:
            if digito in posibles_digitos:
                pass
            else:
                res = 1
                break
        if res:
            return False
        else:
            return True
    else:
        return False
    
def a_base_10(digito):
    if digito in '0123456789':
        return float(digito)
    elif digito in 'aA':
        return 10.
    elif digito in 'bB':
        return 11.
    elif digito in 'cC':
        return 12.
    elif digito in 'dD':
        return 13.
    elif digito in 'eE':
        return 14.
    elif digito in 'fF':
        return 15.
    else:
        return None

def de_base_10(digitos):
    letras = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    if len(digitos) == 1:
        return digitos
    else:
        try:
            return letras[digitos]
        except KeyError:
            return None

def suma_ponderada(entero, decimal, base):
    
    enterorev = entero[::-1]
    base = float(base)
    i = 0
    j = -1
    sumentero = 0.
    sumdecimal = 0.
    for digito in enterorev:
        sumentero = sumentero + (a_base_10(digito) * (base**i))
        i += 1
    for digito in decimal:
        sumdecimal = sumdecimal + (a_base_10(digito) * (base**j))
        j -= 1
    resultado = sumentero + sumdecimal
    return resultado

def division_reiterada(entero, base):
    entero = int(entero)
    base = int(base)
    if entero >= base:
        c , r = (entero/base, entero%base)
        return division_reiterada(c, base) + de_base_10(str(r))
    else:
        return de_base_10(str(entero))

def multiplicacion_reiterada(decimal, base, usados):
    decimal2 = float('0.' + decimal)
    base2 = float(base)
    numero = decimal2 * base2
    entera, dec, sig = descomponer_numero(str(numero))
    usados.append(decimal)
    if dec in usados or float(dec) == 0 or len(usados) > 50:
        return de_base_10(entera)
    else:
        return de_base_10(entera) + multiplicacion_reiterada(dec, base, usados)
            
def base_x_a_base_10(numero, base):
    
    parte_entera, parte_decimal, signo = descomponer_numero(numero)
    resultado = suma_ponderada(parte_entera, parte_decimal, base)
    if signo:
        return resultado
    else:
        return '-' + str(resultado)

def base_10_a_base_x(numero, base):
    
    parte_entera, parte_decimal, signo = descomponer_numero(numero)
    if signo:
        resultado = (division_reiterada(parte_entera, base) + '.' +
         multiplicacion_reiterada(parte_decimal, base, []))
    else:
        resultado = '-' + (division_reiterada(parte_entera, base) + '.' +
         multiplicacion_reiterada(parte_decimal, base, []))
    return resultado
 
def pasar_a_flotante(numero, base, exponente):
    entera, decimal, signo = descomponer_numero(numero)
    if entera == '0':
        if decimal[0] == '0':
            exponente -= 1
            numero = '0.' + decimal[1:]
            return pasar_a_flotante(numero, base, exponente)
        else:
            return (numero, base, exponente)
    else:
        numero = '0.' + entera + decimal
        exponente = len(entera) + exponente
        return pasar_a_flotante(numero, base, exponente) 

def normalizar_por_corte(numero, t):
    entera, decimal, signo = descomponer_numero(numero)
    acortado = entera + '.' + decimal[:t]
    return acortado

def normalizar_por_simetria(numero, base, exponente, t):
    entera, decimal, signo = descomponer_numero(numero)
    nuevo_numero = redondear(decimal, base, t)
    if nuevo_numero:
        if '.' in nuevo_numero:
            numero, base, exp = pasar_a_flotante(nuevo_numero, base, exponente)
            return normalizar_por_simetria(numero, base, exp, t)
        else:
            return '0.' + nuevo_numero, exponente
    else:
        return '0.' + decimal[:t], exponente

def normalizar_num(numero, base, t):
    if verificar_base(numero, '10'):
        numero_convertido = base_10_a_base_x(numero, base)
        num, base, exponente = pasar_a_flotante(numero_convertido, base, 0)
        try:
            t = int(t)
        except:
            t = 0
        if numero[0] == '-':
            flotante = '-%s x %s^%s' %(num, base, exponente)
            if t > 0:
                num_normalizado, exp_normalizado = normalizar_por_simetria(num, 
                    base, exponente, t)
                simetria = '-%s x %s^%s' %(num_normalizado, base, exp_normalizado) 
                corte = '-%s x %s^%s' %(normalizar_por_corte(num, t),
                    base, exponente)
                return (flotante, simetria, corte)
            else:
                return (flotante, 'Nan', 'Nan')
        else:
            flotante = '%s x %s^%s' %(num, base, exponente)
            if t > 0:
                num_normalizado, exp_normalizado = normalizar_por_simetria(num, 
                    base, exponente, t)
                simetria = '%s x %s^%s' %(num_normalizado, base, exp_normalizado) 
                corte = '%s x %s^%s' %(normalizar_por_corte(num, t),
                    base, exponente)
                return (flotante, simetria, corte)
            else:
                return (flotante, 'Nan', 'Nan')
    else:
        return ('NaN', 'NaN', 'NaN')
