#!/usr/bin/env python3

import sys


def read_data(f):
    # Leer del fichero f
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(data):
    # Hacer cosas
    return data


def show_results(nums):
    # Escribir los resultados
    for num in nums:
        print(num)


if __name__ == "__main__":
    data = read_data(sys.stdin)
    # results = process(data)
    show_results(data)

# Para ejecutarlo
# type .\nums\nums10 | python .\lee.py
