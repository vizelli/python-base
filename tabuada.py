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
__version__ = "0.1.0"
__author__ = "Alan"

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do numero: {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
