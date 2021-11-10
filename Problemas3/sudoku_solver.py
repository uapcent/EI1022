import sys
from dataclasses import dataclass

from bt_scheme import DecisionSequence, bt_solve
from sudoku import *


def read_data(f) -> Sudoku:
    lista_cadenas = f.readlines()
    return desde_cadenas(lista_cadenas)


def process(sudoku: Sudoku) -> Iterable[Sudoku]:
    @dataclass
    class Extra:
        sudoku_alm: Sudoku

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku_alm) is None

        def solution(self) -> Sudoku:
            return self.extra.sudoku_alm

        # Para la primera celda vacía, calcular todos los valores posibles
        # Y crear un successor por cada uno
        def successors(self) -> Iterable["SudokuDS"]:
            prim_vac = primera_vacia(self.extra.sudoku_alm)
            if prim_vac is not None:
                nums_disp_casilla = posibles_en(self.extra.sudoku_alm, prim_vac)
                sudoku2 = [f[:] for f in self.extra.sudoku_alm]

                for num in nums_disp_casilla:
                    # Añadir el valor al sudoku Extra2 es el Sudoku con el número insertado Como python funciona por
                    # asignaciones, si hacemos una referencia a sudoku, se modificará el valor en ambos Así que
                    # copiaremos el sudoku
                    sudoku2[prim_vac[0]][prim_vac[1]] = num
                    yield self.add_decision((prim_vac, num), Extra(sudoku2))

    initial_ds = SudokuDS(Extra(sudoku))
    return bt_solve(initial_ds)


def show_results(solutions: Iterable[Sudoku]):
    for solved_sudoku in solutions:
        pretty_print(solved_sudoku)


if __name__ == "__main__":
    sudoku = read_data(sys.stdin)
    sudoku_res = process(sudoku)
    show_results(sudoku_res)