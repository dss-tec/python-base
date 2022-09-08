#!/usr/bin/env python3
""" Tabuada de 1 a 10."""

__version__ = '0.1.0'
__author__ = "Daniel Santos"
__license__ = "Unlicense"

numeros = list(range(1,11))

for numero in numeros:
    print("Tabuada do número {}".format(numero))
    for n in numeros:
        print("{} x {} = {}".format(numero, n, numero * n))
    print(15 * "=")
