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
    diccionario = {}
    for elemento in lista:
        if elemento in diccionario:
            veces = diccionario.get(elemento)
            diccionario[elemento] = veces + 1
        else:
            diccionario[elemento] = 1

    elemento_de_moda = 0
    veces_de_moda = 0
    for k, v in diccionario.items():
        #print(f"Clave {k} | Valor {v}")
        if v > veces_de_moda:
            elemento_de_moda = k
            veces_de_moda = v
    return elemento_de_moda, veces_de_moda


def show_results(repetido, veces):
    # Escribir los resultados
    # for num in nums:
    print(f"El elemento que más se repite es {repetido} ({veces} veces)")


if __name__ == "__main__":
    t0 = time.perf_counter()
    data = read_data(sys.stdin)
    results, amount = process(data)
    show_results(results, amount)
    t1 = time.perf_counter()

    print(f"Tiempo usado: {t1 - t0:f}")

# Usa un conjunto, es mas eficaz, pero ocupa mas. Tiempo por espacio
# Para ejecutarlo
# type .\nums\nums10000 | python .\repetidosOptimizado.py
# Para cronometrar el tiempo
