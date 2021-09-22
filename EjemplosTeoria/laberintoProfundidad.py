from algoritmia.datastructures.digraphs import UndirectedGraph

from typing import *

# Algoritmo recursivo, búsqueda por profundidad

Vertex = Tuple[int, int]


def busca_tesoro_primero_profundidad(lab: UndirectedGraph, v_inicial: Vertex) -> Optional[Vertex]:
    def explorar_desde(v):
        seen.add(v)

        if v == v_tesoro:  # Recorrido en Preorden:
            return v  # Está antes del for
        for suc in lab.succs(v):
            if suc not in seen:
                res = explorar_desde(suc)
                if res is not None:
                    return res
        # if v == v_tesoro:                         # Recorrido en Postorden:
        # return v                                  # Está después del for

    seen = set()
    return explorar_desde(v_inicial)


# Se llama al método recursivo
# Si hay tesoro, termina
# Sino, llama al recursivo para cada habitación no visitada


# Preorden: La primera vez que entramos en una habitación, miramos si hay tesoro
# Postorden: La última vez que entramos en una habitación (no vamos a volver)
#   miramos si tiene tesoro.


# --------Programa principal -------------#
# --------Coste: O( |E| + |V|) -----------#

pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
            ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
            ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

laberinto = UndirectedGraph(E=pasillos)

v_inicio = (0, 0)
v_tesoro = (1, 3)

pos_tesoro_encontrada = busca_tesoro_primero_profundidad(laberinto, v_inicio)

if pos_tesoro_encontrada is None:
    print("Tesoro no encontrado")
else:
    print("Tesoro encontrado en la habitación {0}".format(pos_tesoro_encontrada))
