# C: capacidad
# v: Value
# w: Weight
import sys
from typing import Tuple, List, Optional

Score = int
Decision = int
Solution = Tuple[Score, Optional[List[Decision]]]


def read_data(f) -> Tuple[int, int, List[int], List[List[int]]]:
    U = int(f.readline())
    N = int(f.readline())
    m = [int(w) for w in f.readline().split()]
    v = [[int(w) for w in line.split()]
         for line in f.readlines()
         ]
    return U, N, m, v


def show_results(sol: Solution):
    tv, decisions = sol
    print(tv)
    if decisions is not None:
        for d in decisions:
            print(d)


def resources_direct(U: int, N: int, m: List[int], v: List[List[int]]):
    def S(u: int, n: int) -> Score:
        if n == 0:
            return 0
        if n > 0:
            # Empleamos d unidades, me quedan u - d unidades, tenemos un beneficio de v[n-1, d]
            # Manera compacta
            return max(S(u - d, n - 1) + v[n - 1][d]
                       for d in range(min(m[n - 1], u) + 1))
            # Manera alternativa
            # m = -1
            # for d in range(min(m[n-1], u) +1):
            #     v = S(u-d, n-1)
            #     if v > m:
            #         m = v
            # return m

    return S(U, N), None


def resources_memo(U: int, N: int, m: List[int], v: List[List[int]]):
    def S(u: int, n: int) -> Score:
        if n == 0:
            return 0
        if (u, n) not in mem:
            if n > 0:
                # Empleamos d unidades, me quedan u - d unidades, tenemos un beneficio de v[n-1, d]
                # Manera compacta
                mem[u, n] = max(S(u - d, n - 1) + v[n - 1][d]
                                for d in range(min(m[n - 1], u) + 1)
                                )
        return mem[u, n]

    mem = {}
    return S(U, N), None


def resources_memo_path(U: int, N: int, m: List[int], v: List[List[int]]):
    def S(u: int, n: int) -> Score:
        if n == 0:
            return 0
        if (u, n) not in mem:
            mem[u, n] = max(S(u - d, n - 1) + v[n - 1][d]
                            for d in range(min(m[n - 1], u) + 1)
                            )
        return mem[u, n][0]

    mem = {}
    return S(U, N), None


def resources_iter(U: int, N: int, m: List[int], v: List[List[int]]):
    pass


def resources_iter_red(U: int, N: int, m: List[int], v: List[List[int]]):
    pass


def process(impl: int, U: int, N: int, m: List[int], v: List[List[int]]) -> Solution:
    if impl == 0:
        return resources_direct(U, N, m, v)
    elif impl == 1:
        return resources_memo(U, N, m, v)
    elif impl == 2:
        return resources_memo_path(U, N, m, v)
    elif impl == 3:
        return resources_iter(U, N, m, v)
    elif impl == 4:
        return resources_iter_red(U, N, m, v)
    print(f"Implementacion {impl} no disponible")


# python3 Problemas8/knapsack_pd.py 0 < Problemas5/knapsacks_bab/small.kps
if __name__ == "__main__":
    if len(sys.argv) == 1:  # Si no nos han dado opción, realizamos el caso base
        impl = 0
    else:
        impl = int(sys.argv[1])
    U, N, m, v = read_data(sys.stdin)
    sol = process(impl, U, N, m, v)
    show_results(sol)
