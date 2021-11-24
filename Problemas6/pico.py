import sys
from typing import List


# Si estamos en un valle, y crece hacia la derecha o izquierda, da igual cual de los dos elegir
# Ambos llegarán a un pico --> T(n/2) +1


# def process(v: List[int]) -> int:
#     def pico(i: int, j: int) -> int:
#         if j - i == 1:  # Si nuestro vector tiene un elemento (j apunta fuera)
#             return i
#         m = (i + j) // 2                    # Valor medio
#         if v[m - 1] <= v[m] and v[m] >= v[m + 1]:   # Si es un pico, devolver
#             return m
#         if v[m - 1] <= v[m] <= v[m + 1]:            # Si es un valle, buscamos hacia la derecha, por ejemplo
#             return pico(m + 1, j)
#         return pico(i, j)
#
#     if v[0] >= v[1]:  # Si el primero es pico, hemos terminado
#         return 0
#     if v[-1] >= v[-2]:  # Si el ultimo pico, hemos terminado
#         return len(v) - 1
#     return pico(0, len(v))  # Si no hay picos en los extremos, llamamos a los extremos

def process(v: List[int]) -> int:
    def pico(i: int, j: int) -> int:
        if j - i == 1:  # Si nuestro vector tiene un elemento (j apunta fuera)
            return i
        m = (i + j) // 2  # Valor medio
        if m == 0 and v[m] >= v[m + 1]:
            return m
        if m == len(v) - 1 and v[m] >= v[m - 1]:
            return m
        if v[m - 1] <= v[m] and v[m] >= v[m + 1]:  # Si es un pico, devolver
            return m
        if v[m - 1] <= v[m] <= v[m + 1]:  # Si es un valle, buscamos hacia la derecha, por ejemplo
            return pico(m + 1, j)
        if v[m - 1] >= v[m] >= v[m + 1]:
            return pico(i, m)
        return pico(i, m)

    return pico(0, len(v))  # Si no hay picos en los extremos, llamamos a los extremos


def read_data(f) -> List[int]:
    return [int(l) for l in f.readlines()]


def show_results(pico: int):
    print(pico)


if __name__ == "__main__":
    v = read_data(sys.stdin)
    result = process(v)
    show_results(result, v)
