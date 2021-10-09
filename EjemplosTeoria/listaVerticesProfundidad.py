from typing import Tuple, List

from algoritmia.datastructures.digraphs import Digraph, UndirectedGraph

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def recorredor_vertices_profundidad(grafo: Digraph, v_inicial: Vertex) -> List[Edge]:
    def recorrido_desde(v):
        seen.add(v)
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(suc)

    vertices = []
    seen = set()
    recorrido_desde(v_inicial)
    return vertices


pasillos = [((0, 0), (0, 1)), ((0, 2), (0, 3)), ((1, 0), (1, 1)), ((1, 1), (1, 2)),
            ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((2, 2), (2, 3)), ((0, 1), (1, 1)),
            ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((1, 1), (2, 1)), ((1, 2), (2, 2))]
laberinto = UndirectedGraph(E=pasillos)

v_inicio = (0,0)

lista_vertices = recorredor_vertices_profundidad(laberinto, v_inicio)

print(lista_vertices)
