from LabsSesion2.labyrinthviewer import LabyrinthViewer
from Problemas1.shortest_path import process

if __name__ == '__main__':
    rows = 30
    cols = 50
    addit = 200
    lab, path_prof, path_anch = process(rows, cols, addit)
    lv = LabyrinthViewer(lab, canvas_width=10 * cols,
                         canvas_height=10 * rows)
    lv.add_path(path_prof)
    lv.add_path(path_anch, offset=2, color="blue")
    lv.run()
