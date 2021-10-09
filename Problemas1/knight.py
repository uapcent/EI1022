from typing import Tuple, List
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas1.graph2dviewer import Graph2dViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]
vertices: List[Vertex] = []


def knight_graph(rows: int, cols: int) -> UndirectedGraph:
    # Paso 1: Crea una lista, vertices, con los vértices del grafo (las celdas del
    # laberinto).

    for i in range(rows):
        for j in range(cols):
            vertice: Vertex = (i, j)
            vertices.append(vertice)

    edges: List[Edge] = []
    for x in vertices:
        # Si su vecino horizontal no está fuera
        if x[0] + 1 < rows:
            vecino_horiz: Vertex = (x[0] + 1, x[1])
            arista: Edge = (x, vecino_horiz)
            edges.append(arista)
        if x[1] + 1 < cols:
            vecino_vert: Vertex = (x[0], x[1] + 1)
            arista: Edge = (x, vecino_vert)
            edges.append(arista)

    corridors: List = []
    for arista in edges:
        corridors.append(arista)
    # Paso 6: Construye el grafo y devuélvelo:

    return UndirectedGraph(E=corridors)


def tablero_succs(rows: int, cols: int, first_row: int, first_col: int) -> list[tuple[int, int]]:
    vertices_sin_filtrar = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                            (2, 1), (2, -1), (-2, 1), (-2, -1)]

    vertices_filtrados = []
    for element in vertices_sin_filtrar:
        if element[0] + first_row < rows and element[1] + first_col < cols:
            vertices_filtrados.append(element)
    return vertices_filtrados


def process(rows: int, cols: int, first_row: int, first_col: int):
    tablero = knight_graph(rows, cols)

    def recorrido_desde(u, v):
        vistos.add(v)
        aristas.append((u, v))
        proximos = tablero_succs(rows, cols, v[0], v[1])
        for w in proximos:
            if w not in vistos:
                recorrido_desde(v, w)

    aristas = []
    vistos = set()
    recorrido_desde((first_row, first_col), (first_row, first_col))
    return tablero, len(vistos)
