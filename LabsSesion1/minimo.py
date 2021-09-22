#!/usr/bin/env python3

import sys


def read_data(f):
    # Leer del fichero f
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(lista):
    # Hacer cosas
    m = lista[0]
    for num in data:
        if num < m:
            m = num

    return m


def show_results(num):
    # Escribir los resultados
    print(num)


if __name__ == "__main__":
    data = read_data(sys.stdin)
    results = process(data)
    show_results(results)

# Coste O(n)
# Para ejecutarlo
# type .\LabsSesion1\nums\nums10 | python .\LabsSesion1\minimo.py
