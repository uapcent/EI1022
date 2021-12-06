import sys
from typing import List, Tuple


def read_data(f) -> List[int]:
    return [int(linea) for linea in f.readlines()]


# se le pasa el vector
def process(v: List[int]) -> Tuple[int, int, int]:
    def rec(i: int, j: int) -> Tuple[int, int, int]:
        if j - i == 1:          # Si el vector apuntado es de solo un elemento
            return v[i], i, j   # La suma es el único elemento
        c = (i + j) // 2
        izq = rec(i, c)         # Devuelve la mejor suma a la izq
        der = rec(c, j)         # Devuelve la mejor suma a la derecha
        suma_centro = v[c]
        mejor_centro = v[c]
        begin_centro = c
        end_centro = c + 1
        # Mover desde donde estamos hasta el final
        # Para sacar suma centro, va moviendo de centro a derecha mientras la suma aumente
        for pos in range(c+1, j):
            suma_centro += v[pos]
            # Si la suma es mejor a lo que tenemos
            if suma_centro > mejor_centro:
                mejor_centro = suma_centro
                end_centro = pos + 1
        suma_centro = mejor_centro
        print(f"Para el segundo rango {c} { j -1} la mayor suma es {mejor_centro}")
        # Sacar suma centro, desde el centro hacia izq
        # Voy recorriendo y sumando
        for pos in range(c-1, i-1, -1):     # Vamos de derecha a izq
            suma_centro += v[pos]
            # Si la suma es mejor a lo que tenemos
            if suma_centro > mejor_centro:
                mejor_centro = suma_centro
                begin_centro = pos
        # print(f"Para el primer rango {i} {c-1} la mayor suma es {mejor_centro}")
        # Dos tuplas con [suma, pos_ini, pos_fin]
        # Al ser tuplas, se compara el primer elemento, la suma.
        # print(f"Izq:  {izq} Der: {der} Padre: ( {suma_centro}, {begin_centro}, {end_centro})")
        return max(izq, der, (suma_centro, begin_centro, end_centro))
    return rec(0, len(v))


def show_results(s: int, b: int, e: int):
    print(s)
    print(b)
    print(e)


if __name__ == "__main__":
    vector_puntos = read_data(sys.stdin)
    # vector_puntos = [1, 2, 3, -10, 1, 2, -10, 1]
    s, b, e = process(vector_puntos)
    show_results(s, b, e)
