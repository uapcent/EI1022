# Problema de tiempo, muchas jugadas disponibles
#   Se corta el árbol para no explorarlo t0do
#   Por ejemplo, por profundidad, solo mostrar jugadas que ganen en x rondas
#   Opción 2: Añadir valores a la situación de la partida, para elegir los mejores casos
#   No se garantiza de que se gane siempre

def minimax_move(board: Board, is_max: bool) -> Tuple[Movement, int]:
    # si no hemos terminado
    # Si soy max, cojo max de los mov disponibles
    def go_max(board: Board) -> int:
        if board.is_end():
            return board.evaluate()
        return max(go_min(board.move(m)) for m in board.movements())

    def go_min(board: Board) -> int:
        if board.is_end():
            return board.evaluate()
        return min(go_max(board.move(m)) for m in board.movements())

    if is_max:
        sc, m = max((go_min(board.move(m)), m)
                    for m in board.movements())
    else:
        sc, m = min((go_max(board.move(m)), m)
                    for m in board.movements())
    return m, sc
