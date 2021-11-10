import sys
from dataclasses import dataclass
from typing import List, Iterable, Tuple

from bab_scheme import BoundedDecisionSequence, Solution, bab_max_solve


def knapsack_bab_solve(weights: List[int], values: List[int], capacity: int):
    @dataclass
    class Extra:  # Extra ahorra trabajo, asi no calculamos el peso tot el rato
        weight: int = 0
        value: int = 0

    class KnapsackBDS(BoundedDecisionSequence):
        # Cota optimista: Puedo coger los objetos y cortarlos
        # Dará un objeto mejor de lo posible, pero no se irá mucho
        # Cuanto más bajemos, menos optimista será la cota

        # El objetivo de las cotas es calcular un valor cercano a f, el mejor valor de la mochila.
        def calculate_opt_bound(self) -> int:
            c = capacity - self.extra.weight  # Capacidad restante de la mochila
            v = self.extra.value
            for i in range(len(self), len(weights)):  # Desde el primer objeto restante hasta el final
                if weights[i] <= c:
                    c -= weights[i]
                    v += values[i]
                else:  # Coger una fracción del objeto
                    fr = c / weights[i]
                    v += values[i] * fr
                    break  # Hemos llenado la mochila, c = 0
            return v

        # Cota pesimista: Con los objetos restantes,
        # mirar cuales son los mejores que puede coger
        def calculate_pes_bound(self) -> int:
            c = capacity - self.extra.weight  # Capacidad restante de la mochila
            v = self.extra.value
            for i in range(len(self), len(weights)):  # Desde el primer objeto restante hasta el final
                if weights[i] <= c:
                    c -= weights[i]
                    v += values[i]
            return v  # Como mínimo, tendremos este valor. Pesimista

        def is_solution(self) -> bool:
            return len(self) == len(values)

        def solution(self) -> Solution:
            return self.extra.value, self.extra.weight, self.decisions()

        def successors(self) -> Iterable["KnapsackBDS"]:
            n = len(self)
            if n < len(values):
                if weights[n] <= capacity - self.extra.weight:
                    new_extra = Extra(self.extra.weight + weights[n],
                                      self.extra.value + values[n])
                    yield self.add_decision(1, new_extra)
                yield self.add_decision(0, self.extra)

    initial_ds = KnapsackBDS(Extra())
    return bab_max_solve(initial_ds)


def read_data(f) -> Tuple[int, List[int], List[int]]:
    W = int(f.readline())
    v = []
    w = []
    for linea in f.readlines():
        partes = linea.split()
        v.append(int(partes[0]))
        w.append(int(partes[1]))
    return W, v, w


def show_results(vt: int, pt: int, sol: List[int]):
    print(vt)
    print(pt)
    for d in sol:
        print(d)


if __name__ == "__main__":
    W, v, w = read_data(sys.stdin)
    vt, pt, sol = knapsack_bab_solve(w, v, W)
    show_results(vt, pt, sol)
