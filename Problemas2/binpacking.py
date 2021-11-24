import sys
from random import seed, random
from typing import List


def mientras_quepa(W: List[int], C: int) -> List[int]:
    # W: Recibe x objetos de pesos varoables
    #       (1,2,8,7,8,3) --> 6 objetos y sus pesos
    # C: Capacidad de los contenedores
    # Devuelve una lista indicando a que posicion va cada objeto

    # Mientras quepa:
    #   Se abre el primer contenedor
    #   Se depositan los objetos hasta que uno no quepa
    #   Se cierra el contenedor, se abre y se repite

    # pos_actual = 0
    # contenedores = []  # Cada elemento es un contenedor, se guarda el peso de cada uno
    # lista_contenedor = []  # para cada objeto, se indica en que contenedor se guarda
    #
    # for i in range(len(W)):
    #     if contenedores[pos_actual] + W[i] <= C:  # Si cabe el objeto
    #         contenedores[pos_actual] += W[i]  # metemos el objeto al almacen, subiendo el peso
    #         lista_contenedor[i] = pos_actual  # Decimos que el objeto W[i] está en el contenedor actual
    #     else:
    #         pos_actual += 1  # Si no cabe, abrimos un nuevo contenedor
    # return lista_contenedor

    res = []
    c = 0
    ocupado = 0
    for peso in W:
        if ocupado+peso > C:
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
    indices_ordenados = sorted(range(len(W)), key= lambda i: -W[i])
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
    alg = int(f.readline())
    c = int(f.readline())
    w = [int(line) for line in f.readlines()]
    # w = []
    # for line in f.readlines():
    #     w.append(int(line))

    return alg, c, w


def process(alg: int, C: int, W: List[int]) -> List[int]:
    if alg == 0:
        return mientras_quepa(W, C)
    elif alg == 1:
        return primero_que_quepa(W, C)
    elif alg == 2:
        return primero_que_quepa_ordenado(W, C)

    # Successors:


def show_results(res: List[int]):
    for c in res:
        print(c)


if __name__ == "__main__":
    # alg, C, W = read_data(sys.stdin)
    # lista = process(alg, C, W)
    # show_results(lista)

    seed(42)
    w = [int(random() * 1000) + 1 for i in range(1000)]
    c = 1100
    print(f"Como líquido: {(sum(w) + c - 1) // c}")
    for algorithm, sol in [(0, 637), (1, 497), (2, 474)]:
        res = process(algorithm, c, w)
    nc = max(res) + 1
    print(f"Algoritmo {algorithm}: {nc}", end=" ")
    if nc != sol:
        print(f"Error: esperado {sol}")
    else:
        print("OK")
