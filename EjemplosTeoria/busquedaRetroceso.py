from dataclasses import dataclass
from typing import Tuple, Iterable

from EjemplosTeoria.bt_scheme import DecisionSequence, bt_solve


def coin_change_solve(v: Tuple[int, ...], Q: int):
    @dataclass
    class Extra:
        pending: int

    class CoinChangeDS(DecisionSequence):
        # True si el estado actual es una sol correcta
        # False si no lo es
        # En este caso, si hemos recorrido todas las monedas y no nos queda dinero que repartir...
        def is_solution(self) -> bool:
            return len(self) == len(v) and self.extra.pending == 0

        # Generador, devuelve Iterable, no se le puede poner Return None
        # Devuelve las decisiones que se generan a partir de la actual, tomando todas las validas
        def successors(self) -> Iterable["CoinChangeDS"]:
            # Numero de iteraciones o pasos
            n = len(self)
            # Si aun quedan elementos por comprobar
            if n < len(v):
                for num_coins in range(self.extra.pending // v[n] + 1):
                    # Calcula el dinero restante por repartir
                    p2 = self.extra.pending - num_coins * v[n]
                    yield self.add_decision(num_coins, Extra(p2))

    # Devuelve un generador, siempre son estas dos lineas
    initial_ds = CoinChangeDS(Extra(Q))
    # bt_solve: Recibe la DecisionSequence inicial, genera y recorre el grafo, y devuelve iterador de soluciones
    return bt_solve(initial_ds)


coins, quantity = (1, 2, 5, 10), 11
for sol in coin_change_solve(coins, quantity):
    print(sol)
