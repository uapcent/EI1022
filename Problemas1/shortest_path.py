from typing import Tuple, List

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from Problemas1.labyrinth import create_labyrinth

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


#  hace un recorrido primero en profundidad desde source y
# que se detiene en el momento en que encuentra target

def df_search(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    def recorrido_desde(u, v):
        vistos.add(v)
        aristas.append((u, v))
        if v == target:
            return
        for w in g.succs(v):
            if w not in vistos:
                recorrido_desde(v, w)

    aristas = []
    vistos = set()
    recorrido_desde(source, source)
    return aristas


# Recorrido en anchura hasta que encuentra el elemento
def bf_search(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        if v == target:
            return aristas
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas


# a partir del resultado de df_search devuelve el camino hasta target
def recover_path(edges: List[Edge], target: Vertex) -> List[Vertex]:
    anterior = {}
    for u, v in edges:
        anterior[v] = u
    camino = [target]
    u = target
    while u != anterior[u]:
        u = anterior[u]
        camino.append(u)
    camino.reverse()
    return camino

    # bp = {}
    # for orig, dest in edges:
    #     bp[dest] = orig
    # # Reconstruye el camino yendo hacia atrás
    # camino = [target]
    # while target != bp[target]:
    #     target = bp[target]
    #     camino.append(target)
    # # Invierte el camino ya que lo hemos obtenido al revés
    # camino.reverse()
    # return camino


# Prueba del recorrido
def read_data(f):
    rows = int(f.readLine())
    cols = int(input("Número de columnas: "))
    additional = int(input("Número de pasillos extra: "))
    return rows, cols, additional


def process(rows: int, cols: int, addit: int):
    labyrinth = create_labyrinth(rows, cols, addit)
    start_coords = (0, 0)
    end_coords = (rows - 1, cols - 1)

    edge_list_prof = df_search(labyrinth, start_coords, end_coords)
    edge_list_anch = bf_search(labyrinth, start_coords, end_coords)
    path_profund = recover_path(edge_list_prof, end_coords)
    path_anchura = recover_path(edge_list_anch, end_coords)

    return labyrinth, path_profund, path_anchura


def show_results(l: list[tuple[int, int]]):
    for element in l:
        print(element)


if __name__ == '__main__':
    n_rows, n_cols, n_addit = read_data()
    lab, path_prof, path_anch = process(n_rows, n_cols, n_addit)
    show_results(path_prof)
