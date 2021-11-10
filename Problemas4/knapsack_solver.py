import sys
from typing import Iterable, Tuple, List
from dataclasses import dataclass
from bt_scheme import ScoredDecisionSequence, State, bt_max_solve


def read_data(f) -> Tuple[int, List[int], List[int]]:
    W = int(f.readline())
    v = []
    w = []
    for linea in f.readlines():
        partes = linea.split()
        v.append(int(partes[0]))
        w.append(int(partes[1]))
    return W, v, w


# con backtracking miraremos muchas mochilas, y nos quedaremos al mejor
# Solo miraremos hijos SI tiene posibilidades de ser mejor a la que ya tenemos
# Se compara en el mismo estado, llevan la misma cantidad de objetos visitados
# El estado en una mochila son los objetos visitados y la cantidad que queda

# Hay que implementar el control de visitados, podemos encontrar mochilas iguales
# Usaremos el método state()
# W: Capacidad, v: Lista valores, w: Lista pesos

# KnapsackDs es una mochila, cuando he visto todos los objetos, len(self) == len(v)
def process(W, v: List[int], w: List[int]):
    @dataclass
    class Extra:
        libre: int  # Peso restante que puede llevar una mochila
        valor: int  # Valor actual de la mochila

    class KnapsackDS(ScoredDecisionSequence):
        def is_solution(self) -> bool:
            return len(self) == len(v)

        # Si he visto todos los objetos, no hago nada. Dos opciones:
        #   if not self.is_solution
        #   if len(self) < len(v)
        # Las decisiones son 0 o 1
        #   0: No se coge elemento, no cambia Extra
        #   1: Se coge elemento, se pasa al siguiente elemento con Extra cambiado
        def successors(self) -> Iterable["KnapsackDS"]:
            if not self.is_solution():
                # Dos decisiones, coger objeto o no cogerlo
                yield self.add_decision(0, self.extra)
                i = len(self)
                if w[i] <= self.extra.libre:
                    yield self.add_decision(1, Extra(self.extra.libre - w[i],
                                                     self.extra.valor + v[i]))

        # Para decidir que mochila es mejor
        # Score: Valor de los objetos metidos
        # Puedes recorrer las decisiones, sumar el valor para cada objeto
        # O simplemente devolver extra
        def score(self) -> int:
            return self.extra.valor

        # que es el estado? Para comparar mochilas
        # Qué tengo que saber de las mochilas, para saber que una es mejor que otra
        # Hace falta saber cuanto hueco tengo, y los objetos que quedan por mirar
        def state(self) -> State:
            return self.extra.libre, len(self)

    # Secuencia inicial, una mochila que empeiza con tot el peso libre, y 0 de valor
    # irá devolviendo soluciones, y cada una es mejor que la anterior
    # Tenemos que quedarnos con la última, la mejor
    initial_ds = KnapsackDS(Extra(W, 0))
    sol = None  # Almacenará la última solución, la mejor
    for sol in bt_max_solve(initial_ds):
        pass
    valor_total = 0
    peso_total = 0
    for i in range(len(sol)):
        valor_total += sol[i] * v[i]
        peso_total += sol[i] * w[i]

    # for i, d in enumerate(sol):
    #   valor_total += sol[i] * v[i]
    #   peso_total += sol[i] * w[i]

    return valor_total, peso_total, sol


def show_results(vt: int, pt: int, sol: List[int]):
    print(vt)
    print(pt)
    for d in sol:
        print(d)


if __name__ == "__main__":
    W, v, w = read_data(sys.stdin)
    vt, pt, sol = process(W, v, w)
    show_results(vt, pt, sol)
