import sys
from typing import List, Tuple, Optional

Score = int
Decision = int
Solution = Tuple[Score, Optional[List[Decision]]]


# C: capacidad
# v: Value
# w: Weight
def read_data(f) -> Tuple[int, List[int], List[int]]:
    C = int(f.readline())
    v = []
    w = []
    for linea in f.readlines():
        partes = linea.split()
        v.append(int(partes[0]))
        w.append(int(partes[1]))
    return C, v, w


def show_results(sol: Solution):
    tv, decisions = sol
    print(tv)
    if decisions is not None:
        for d in decisions:
            print(d)


# Tiene alto coste, se hacen dos llamadas recursivas en cada iteración
# Hay varios estados que son los mismos, memorizamos las combinaciones de c y n, su max beneficio
def knapsack_direct(w: List[int], v: List[int], C: int) -> Solution:
    # c: Capacidad restante
    # n: Numero del objeto apuntado / restantes
    def S(c: int, n: int):
        if n == 0:
            return 0
        if n > 0 and w[n - 1] <= c:
            # capacidad no cambia, dejamos el objeto  / Capacidad disminuye, un objeto menos, más valor
            return max(S(c, n - 1), (S(c - w[n - 1], n - 1) + v[n - 1]))
        if n > 0 and w[n - 1] > c:
            return S(c, n - 1)

    return S(C, len(v)), None  # Se devuelve none porque no sabes el camino


# Buscamos la combinación en un diccionario, si está, se devuelve el valor
# Sino, se almacena y se devuelve
def knapsack_memo(w: List[int], v: List[int], C: int):
    # c: Capacidad restante
    # n: Numero del objeto apuntado / restantes
    def S(c: int, n: int):
        if n == 0:
            return 0
        if (c, n) not in mem:
            if n > 0 and w[n - 1] <= c:
                # capacidad no cambia, dejamos el objeto  / Capacidad disminuye, un objeto menos, más valor
                mem[c, n] = max(S(c, n - 1), (S(c - w[n - 1], n - 1) + v[n - 1]))
            if n > 0 and w[n - 1] > c:
                mem[c, n] = S(c, n - 1)
        return mem[c, n]

    mem = {}
    return S(C, len(v)), None  # Se devuelve none porque no sabes el camino


# Nos guardaremos el valor, el anterior y la decision para llegar ahi
def knapsack_memo_path(w: List[int], v: List[int], C: int):
    # c: Capacidad restante
    # n: Numero del objeto apuntado / restantes
    def S(c: int, n: int):
        if n == 0:
            return 0
        if (c, n) not in mem:
            if n > 0 and w[n - 1] <= c:
                # capacidad no cambia, dejamos el objeto  / Capacidad disminuye, un objeto menos, más valor
                mem[c, n] = max((S(c, n - 1), (c, n - 1), 0),
                                (S(c - w[n - 1], n - 1) + v[n - 1], (c - w[n - 1], n - 1), 1)
                                )
            if n > 0 and w[n - 1] > c:
                # He venido de c, n -1, he tomado la decision de dejarlo en el suelo (0)
                mem[c, n] = (S(c, n - 1), (c, n - 1), 0)
        return mem[c, n][0]

    # En mem tenemos info adicional que permite recuperar el camino
    mem = {}
    score = S(C, len(v))
    path = []
    # Almacenamos la celda que corresponde al ultimo objeto, y se va tirando hacia atrás y rellenando el path
    c, n = C, len(v)
    # Append al final es lineal, al principio no. Y Reverse también es lineal
    while n > 0:
        path.append(mem[c, n][2])
        # El valor anterior de c, n
        c, n = mem[c, n][1]
    path.reverse()  # El camino ha sido añadido al reves, damos al vuelta
    return score, path  # Se devuelve none porque no sabes el camino


# en algunos casos, la manera iterativa es más eficiente
def knapsack_iter(w: List[int], v: List[int], C: int):
    # c: Capacidad restante
    # n: Numero del objeto apuntado / restantes
    mem = {}
    for c in range(C + 1):
        for n in range(len(v) + 1):
            if n == 0:
                # No hay decisiones
                mem[c, n] = 0, None, None
            if n > 0 and w[n - 1] <= c:
                # capacidad no cambia, dejamos el objeto  / Capacidad disminuye, un objeto menos, más valor
                mem[c, n] = max((mem[c, n - 1], (c, n - 1), 0),
                                (mem[c - w[n - 1], n - 1][0] + v[n - 1], (c - w[n - 1], n - 1), 1)
                                )
            if n > 0 and w[n - 1] > c:
                # He venido de c, n -1, he tomado la decision de dejarlo en el suelo (0)
                mem[c, n] = (S(c, n - 1), (c, n - 1), 0)

        return mem[c, n][0]

    # En mem tenemos info adicional que permite recuperar el camino

    score = mem[C, len(v)][0]
    path = []
    # Almacenamos la celda que corresponde al ultimo objeto, y se va tirando hacia atrás y rellenando el path
    c, n = C, len(v)
    # Append al final es lineal, al principio no. Y Reverse también es lineal
    while n > 0:
        path.append(mem[c, n][2])
        # El valor anterior de c, n
        c, n = mem[c, n][1]
    path.reverse()  # El camino ha sido añadido al reves, damos al vuelta
    return score, path  # Se devuelve none porque no sabes el camino


def knapsack_iter_red(w, v, C):
    pass


def process(impl: int, C: int, v: List[int], w: List[int]) -> Solution:
    if impl == 0:
        return knapsack_direct(w, v, C)
    elif impl == 1:
        return knapsack_memo(w, v, C)
    elif impl == 2:
        return knapsack_memo_path(w, v, C)
    elif impl == 3:
        return knapsack_iter(w, v, C)
    elif impl == 4:
        return knapsack_iter_red(w, v, C)
    print(f"Implementacion {impl} no disponible")


# python3 Problemas8/knapsack_pd.py 0 < Problemas5/knapsacks_bab/small.kps
if __name__ == "__main__":
    if len(sys.argv) == 1:  # Si no nos han dado opción, realizamos el caso base
        impl = 0
    else:
        impl = int(sys.argv[1])
    W, v, w = read_data(sys.stdin)
    sol = process(impl, W, v, w)
    show_results(sol)
