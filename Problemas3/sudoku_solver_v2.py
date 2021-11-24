import sys
from dataclasses import dataclass

from bt_scheme import DecisionSequence, bt_solve, Decision
from sudoku import *


def read_data(f) -> Sudoku:
    lista_cadenas = f.readlines()
    return desde_cadenas(lista_cadenas)


def process(sudoku: Sudoku) -> Iterable[Sudoku]:
    @dataclass
    class Extra:
        sudoku_alm: Sudoku
        cel_vac: [Position]

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku_alm) is None

        def solution(self) -> Sudoku:
            return self.extra.sudoku_alm

        # Para la primera celda vacía, calcular todos los valores posibles
        # Y crear un successor por cada uno
        def successors(self) -> Iterable["SudokuDS"]:
            prim_vac = primera_vacia(self.extra.sudoku_alm)
            if prim_vac is not None:  # Si hay celdas vacías
                self.extra.cel_vac = posibles_en(self.extra.sudoku_alm,
                                                 prim_vac)  # Devuelve todos los numeros en una decision

                for num in self.extra.cel_vac:
                    self.extra.sudoku_alm[prim_vac[0]][prim_vac[1]] = num
                    yield self.add_decision((prim_vac, num), self.extra)

                # Para reutilizar el Extra, y no crear copias
                self.extra.sudoku_alm[prim_vac[0]][prim_vac[1]] = 0
            # Cuando se hace yield, se vuelve a llamar a bt_solve, hasta que se llenen los huecos
            # Cuando termine de llenarse en el yield, se ejecutará con el siguiente número

    initial_ds = SudokuDS(Extra(sudoku))
    return bt_solve(initial_ds)


def show_results(solutions: Iterable[Sudoku]):
    for solved_sudoku in solutions:
        pretty_print(solved_sudoku)


if __name__ == "__main__":
    sudoku = read_data(sys.stdin)
    sudoku_res = process(sudoku)
    show_results(sudoku_res)
