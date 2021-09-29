from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from typing import *

# Algoritmo no recursivo, usa una cola FIFO

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def busca_tesoro_primero_anchura(lab: UndirectedGraph, v_inicial: Vertex) -> Optional[Vertex]:
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)       # Meter a la pila la posición inicial
    seen.add(v_inicial)         # Poner como visitado al inicial
    while len(queue) > 0:       # Sacar un elemento de la pila
        v = queue.pop()
        if v == v_tesoro:                   # Si tiene tesoro, devuelve posicion y para la búsqueda
            return v
        for suc in lab.succs(v):            # Recorremos todos sus adyacentes
            if suc not in seen:             # Si no los hemos visitado, los metemos a la pila y a visitados
                seen.add(suc)
                queue.push(suc)
    return None


# --------Programa principal -------------#
# --------Coste: O( |E| + |V|) -----------#

pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
            ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
            ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]

laberinto = UndirectedGraph(E=pasillos)

v_inicio = (0, 0)
v_tesoro = (1, 3)

pos_tesoro_encontrada = busca_tesoro_primero_anchura(laberinto, v_inicio)

if pos_tesoro_encontrada is None:
    print("Tesoro no encontrado")
else:
    print("Tesoro encontrado en la habitación {0}".format(pos_tesoro_encontrada))
