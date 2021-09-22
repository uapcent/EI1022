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
    repeated = False
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                repeated = True

    return repeated


def show_results(repetido):
    # Escribir los resultados
    #for num in nums:
    print("Hay repetidos" if repetido else "No hay repetidos")


if __name__ == "__main__":
    t0 = time.perf_counter()
    data = read_data(sys.stdin)
    results = process(data)
    show_results(results)
    t1 = time.perf_counter()

    print(f"Tiempo usado: {t1 - t0:f}")

# Coste O(n^2) cuadrático, hay un bucle dentro del bucle. Sol: sacar el average
# Para ejecutarlo
# type .\nums\nums10 | python .\minimo.py
# Para cronometrar el tiempo
