#!/usr/bin/python
"""Programa que imprime a tabuada do 1 ao 10.

Tabuada do 1:
1
2
3
4
...
------------
Tabuada do 2:
2
4
6
...
"""
__version__ = "0.0.1"
__author__ = "Alan"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do numero:",numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------")
