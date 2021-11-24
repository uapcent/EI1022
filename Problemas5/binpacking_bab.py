import sys
from dataclasses import dataclass
from random import seed, random
from typing import List

from bab_scheme import BoundedDecisionSequence


def mientras_quepa(W: List[int], C: int) -> List[int]:
    res = []
    c = 0
    ocupado = 0
    for peso in W:
        if ocupado + peso > C:
            # Si no cabe en uno nuevo
            c += 1
            ocupado = 0
        ocupado += peso
        res.append(c)

    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    res = []
    ocupado = []
    for peso in W:

        for c in range(len(ocupado)):
            if ocupado[c] + peso <= C:  # Cabe
                break
        else:
            # Meto en una nueva
            c = len(ocupado)
            ocupado.append(0)
        ocupado[c] += peso
        res.append(c)
    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    # Ordenar y llamar al metodo anterior y luego recompones
    # Si reordenas los objetos, las posiciones de la lista no encajan
    res = [0] * len(W)
    ocupado = []
    indices_ordenados = sorted(range(len(W)), key=lambda i: -W[i])
    for i in indices_ordenados:
        peso = W[i]
        encontrado = False
        for c in range(len(ocupado)):
            if ocupado[c] + peso <= C:
                encontrado = True
                break
        if not encontrado:
            c = len(ocupado)
            ocupado.append(0)
        ocupado[c] += peso
        res[i] = c
    return res

    pass


def read_data(f):
    c = int(f.readline())
    w = [int(line) for line in f.readlines()]
    return c, w


def process(capacity: int, W: List[int]) -> List[int]:
    @dataclass
    class Extra:  # Extra ahorra trabajo, asi no calculamos el peso tot el rato
        contenedores: List[int]
        weight: int = 0

    class BinpackingDS(BoundedDecisionSequence):
        def calculate_opt_bound(self) -> int:
            for i in range(len(self.extra.contenedores)):
                for j in range(len(W)):
                    if W[j] <= self.extra.contenedores[i]:
                        pass

            pass

        def calculate_pes_bound(self) -> int:

            pass


def show_results(res: List[int]):
    for c in res:
        print(c)


if __name__ == "__main__":
    C, W = read_data(sys.stdin)
    lista = process(C, W)
    show_results(lista)
