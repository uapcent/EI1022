import sys
from typing import *
from random import shuffle
from labyrinthviewer import LabyrinthViewer


# Creamos alias para los tipos de los vértices y de las aristas
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

# Ahora Vertex y Edge se pueden usar como cualquier tipo:
vertices: List[Vertex] = []


# Leer el número de filas y columnas del laberinto
def read_data(f: TextIO):
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(num_rows: int, num_columns: int):
    # Paso 1: Crea una lista, vertices, con los vértices del grafo (las celdas del
    # laberinto).

    for i in range(num_rows):
        for j in range(num_columns):
            vertice: Vertex = (i, j)
            vertices.append(vertice)

    # print(vertices)

    # Paso 2: Usa MergeFindSet(), de
    # algoritmia.datastructures.mergefindsets para crear un MFSet
    # vacío, mfs. Añade los vértices de vertices usando mfs.add(·).

    mfs: MergeFindSet = MergeFindSet()
    for i in vertices:
        mfs.add(i)

    # print(mfs)

    # Paso 3: Crea una lista, edges, con todos los pares de vértices vecinos y
    # barájala. Usa la función shuffle del módulo random.

    edges: List[Edge] = []
    for x in vertices:
        # Si su vecino horizontal no está fuera
        if x[0]+1 < num_rows:
            # print('{0} es menor que {1}'.format(x[0]+1, num_rows))
            vecino_horiz: Vertex = (x[0] + 1, x[1])
            # print('El vecino h de {0} es {1}'.format(x, vecino_horiz))
            arista: Edge = (x, vecino_horiz)
            edges.append(arista)
        if x[1]+1 < num_columns:
            # print('{0} es menor que {1}'.format(x[1]+1, num_rows))
            vecino_vert: Vertex = (x[0], x[1]+1)
            # print('El vecino v de {0} es {1}'.format(x, vecino_vert))
            arista: Edge = (x, vecino_vert)
            edges.append(arista)

    shuffle(edges)

    # Paso 4: Crea una lista vacía, corridors. Aquí pondremos las aristas
    # (pasillos) que tendrá al final nuestro grafo (laberinto).
    corridors: List = []

    # Paso 5: Recorre la lista edges y, para cada arista (u,v), encuentra la
    # clase a la que pertenece cada uno de los dos vértices usando
    # mfs.find(·). Si son diferentes, fusiónalas en la misma clase con
    # mfs.merge(u, v) y añade la arista (u,v) a la lista corridors.

    for arista in edges:
        print(mfs.find(arista[0]))
        print(mfs.find(arista[1]))
        if mfs.find(arista[0]) != mfs.find(arista[1]):
            mfs.merge(arista[0], arista[1])
            corridors.append(arista)
    # Paso 6: Construye el grafo y devuélvelo:

    return UndirectedGraph(E=corridors)

    # Como se sabe que no se cren ciclos? Cada grupo de caminos es un conjunto, cada vértice también, solo se
    # pueden unir dos de distintos cojuntos
    # Cuando se generan vértices al azar, se ahcen 2 finds, si estan en conjuntos distintos, se juntan, sino repetir
    # merge si estan en distintos --> Usamos MFSet, estructura de datos pensada en MergesFind y muy optimizadas.


# Escribe el grafo por pantalla
def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


# Programa principal
if __name__ == "__main__":
    # rows, cols = read_data(sys.stdin)
    # labyrinth = process(rows, cols)
    # show_results(labyrinth)
    cols = 150
    rows = 60
    labyrinth = process(rows, cols)
    lv = LabyrinthViewer(labyrinth, canvas_width=10 * cols,
                         canvas_height=10 * rows)
    lv.run()
