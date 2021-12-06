import sys
from typing import List, Tuple

from bt_scheme import infinity


def read_data(f) -> List[int]:
    return [int(linea) for linea in f.readlines()]


# se le pasa el vector
def process(v: List[int]) -> Tuple[int, int, int]:
    def div_solve(start: int, end: int) -> Tuple[int, int, int]:
        ne = end - start
        if ne == 1:
            return v[start], start, start + 1  # Se devuelve, la suma, b, e (la e es siempre el siguiente al que apunta)
        else:
            # Divide y combina ( dos llamadas recursivas)
            h = (start + end) // 2
            best_left = div_solve(start, h)
            best_right = div_solve(h, end)

            # Encontrar el mejor por la derecha
            best_right_value = -infinity
            best_right_index = None
            acu = 0
            for i in range(h, end):
                acu += v[i]
                if acu >= best_right_value:
                    best_right_value = acu
                    best_right_index = i

            # Encontrar el mejor por la izquierda
            best_left_value = v[h-1]
            best_left_index = h-1
            acul = v[h-1]
            for j in range(h - 2, start - 1, -1):
                acul += v[j]
                if acul >= best_left_value:
                    best_left_index = j
                    best_left_value = acul

            best_center = (best_left_value + best_right_value, best_left_index, best_right_index+1)
            # Valor absurdo, no se sabe calcular por el momento

            # Devolver la solución: (suma,b,e)
            return max(best_left, best_right, best_center)

    return div_solve(0, len(v))


def show_results(s: int, b: int, e: int):
    print(s)
    print(b)
    print(e)


if __name__ == "__main__":
    vector_puntos = read_data(sys.stdin)
    # vector_puntos = [1, 2, 3, -10, 1, 2, -10, 1]
    s, b, e = process(vector_puntos)
    show_results(s, b, e)
