#!/usr/bin/env python3

import sys
import time


def read_data(f):
    # Leer del fichero f
    # En l tenemos una cadena por línea:
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(lista):
    sums = set()
    for num in lista:
        for s in list(sums):
            sums.add(s+num)
        sums.add(num)
    return len(sums)


def show_results(repetido):
    # Escribir los resultados
    # for num in nums:
    print(repetido)


if __name__ == "__main__":
    t0 = time.perf_counter()
    data = read_data(sys.stdin)
    results = process(data)
    show_results(results)
    t1 = time.perf_counter()

    print(f"Tiempo usado: {t1 - t0:f}")

# Usa un conjunto, es mas eficaz, pero ocupa mas. Tiempo por espacio
# Para ejecutarlo
# type .\nums\nums10000 | python .\repetidosOptimizado.py
# Para cronometrar el tiempo
