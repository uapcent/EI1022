# Para conseguir el camino a un punto en un grafo a partir de uno inicial
from typing import Tuple, List

from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph
from algoritmia.datastructures.queues import Fifo

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


# Necesitamos:
# Un recorredor que devuelva la lista de aristas del recorrido

def recorrido_aristas_anchura(grafo: Digraph, v_inicial: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))  # La primera arista es fantasma
    seen.add(v_inicial)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    print(aristas)
    return aristas


# Un algoritmo trivial que dada la lista anterior y el vértice al que queremos llegar
#   recupera el camino (lista de vértices). El perfil es:
def recuperador_camino(lista_aristas: List[Edge], v: Vertex) -> List[Vertex]:
    # Crear un diccionario de punteros hacia atrás (backpointers)
    bp = {}
    for orig, dest in lista_aristas:        # Almacenamos cada arista como destino: origen
        bp[dest] = orig
    # Reconstruye el camino yendo hacia atrás
    camino = []
    camino.append(v)                        # Ponemos el destino como primer elemento
    while v != bp[v]:                       # El primer elemento de la lista aristas es el fantasma
        v = bp[v]                           # Si llegamos a ese, hemos terminado,  sino
        camino.append(v)                    # mientras actual != anterior, actual = anterior
    # Invierte el camino ya que lo hemos obtenido al revés
    camino.reverse()
    return camino


# PROGRAMA PRINCIPAL

pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
            ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
            ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]
laberinto = UndirectedGraph(E=pasillos)
v_inicio = (0, 0)
v_tesoro = (1, 3)

a = recorrido_aristas_anchura(laberinto, v_inicio)
print(recuperador_camino(a, v_tesoro))
