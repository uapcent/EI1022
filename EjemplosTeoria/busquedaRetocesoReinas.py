from collections import Iterable

from EjemplosTeoria.bt_scheme import bt_solve, DecisionSequence, Solution


def nqueens_solve(n: int) -> Iterable[Solution]:
    class NQueensDS(DecisionSequence):
        def is_solution(self) -> bool:
            return len(self) == n

        def successors(self) -> Iterable["NQueensDS"]:
            t = len(self)
            if t < n:
                decisions = self.decisions()
                for row in range(n):
                    # Si no se han colocado tantas reinas como filas
                    # Y no hay reinas en diagonal?
                    if all(r != row and t - j != abs(row - r)
                           for j, r in enumerate(decisions)):
                        yield self.add_decision(row)

    initial_ds = NQueensDS()
    return bt_solve(initial_ds)


# How to use the function ----------------------------
n = 4
for sol in nqueens_solve(n):
    print(sol)
