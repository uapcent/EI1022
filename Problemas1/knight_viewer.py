from algoritmia.datastructures.digraphs import UndirectedGraph

from Problemas1 import knight
from Problemas1.graph2dviewer import Graph2dViewer


def read_data():
    rows = 8
    cols = 8
    first_row = 4
    first_col = 4
    return rows, cols, first_row, first_col


def process(rows: int, cols: int, first_row: int, first_col: int):
    grafo, num_casillas = knight.process(rows, cols, first_row, first_col)

    return grafo, num_casillas


def show_results(board: UndirectedGraph):
    viewer = Graph2dViewer(board, vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()


if __name__ == "__main__":
    rows, cols, first_row, first_col = read_data()
    tablero, num = process(rows, cols, first_row, first_col)
    print(num)
    show_results(tablero)
