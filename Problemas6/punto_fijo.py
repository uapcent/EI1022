# lee de su
# entrada estándar un vector de enteros en formato un número
# por línea y escribe por su salida estándar No hay punto
# fijo si el vector no tiene punto fijo o el valor del punto fijo si
# lo tiene

# [2, 3, 3, 4, 5, 10] mal, nums repetidos
# Si en la pos 0 hay un 2, cuando avance tendre minimo 2 mas que el indice, pero el indice nunca será igual al valor
# [100, 101, 102, 103] Bien Sabemos que no hay punto fijo, porque nunca se alcanzará

# [1, -10, 5, 6] mal, no ordenado
# [2, 3, 4, 5, 6, 7],  bien
# [-6, -5, -4, -3] bien
# Si la pos 0 es -6, la pos 1 puede ser 1,
# se puede mirar la más grande (-3) yo retrocedo y el índice retrocede.

# Sabemos que estan ordenados, y que son distintos, mirando
# una pos se puede saber si hay puntos fijos

# Lo normal en divide y vencerás es mirar el centro (y los de al lado si hace falta).
# Decidir si hacia la izquierda o derecha hay punto fijo
#  [-10, -5, 1, 3, 6]
# A la izquierda no puede estar, buscamos hacia la derecha --> 3 es punto fijo
import sys

from dac_scheme import *


def read_data(f) -> List[int]:
    return [int(linea) for linea in f.readlines()]


def process(vector: List[int]) -> Optional[int]:
    def punto_fijo(start: int, end: int):
        h = (start + end) // 2
        if vector[h] == h:      # Si es punto fijo, devolver
            return h
        # if start >= end
        if h == start:          # Si el vector está vacio, no hay ningun punto fijo
            return None
        if vector[h] < h:       # Si, el elemento en la mitad es mas pequeño, la intersección estará por la derecha
            return punto_fijo(h + 1, end)   # Buscamos en la segunda mitad
        if vector[h] > h:       # Buscamos en la primera mitad
            return punto_fijo(start, h)

    return punto_fijo(0, len(vector))   # Mirar vector entero, hasta len(v) (primer indice fuera) asi evitamos poner -1


def show_results(result: Optional[int]):
    if result is None:
        print("No hay punto fijo")
    else:
        print(result)


if __name__ == "__main__":
    vector_puntos = read_data(sys.stdin)
    tiene_punto_fijo = process(vector_puntos)
    show_results(tiene_punto_fijo)
