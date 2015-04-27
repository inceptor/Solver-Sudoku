__author__ = 'Inceptor'

'''def resolve(sudoku):

    for ligne in range(9):
        for col in range(9):
            if sudoku.area[ligne][col] != 0:
                continue
            for nbre in range(1,10):
                if not case_dispo_nbre(sudoku, nbre, ligne, col):
                    continue

                nbre_tamp = sudoku.area[ligne][col]
                sudoku.area[ligne][col] = nbre
                sudoku.print()
                resolve(sudoku)
                if grille_finie(sudoku):
                    return

                sudoku.area[ligne][col] = nbre_tamp
            return
    return


def case_dispo_nbre(sudoku, nbre, ligne, col):
    tamp = []
    for i in range(9):
        if sudoku.area[ligne][i] == nbre:
            return False

    for i in range(9):
        if sudoku.area[i][col] == nbre:
            return False

    tamp = trans_carre_de_case(sudoku, tamp, ligne, col)

    for i in range(9):
        if tamp[i] == nbre:
            return False

    return True

def trans_carre_de_case(sudoku, tamp, ligne, col):

    while ((ligne % 3) != 0):
        ligne -= 1

    while ((col % 3) != 0):
        col -= 1

    for j in range(ligne+3):
        for i in range(col+3):
            tamp.append(sudoku.area[j][i])

    return tamp

def grille_finie(sudoku):
    for ligne in range (9):
        for col in range(9):
            if sudoku.area[ligne][col] == 0:
                return False
    return True'''


class Case:
    def __init__(self, i = 0, j = 0,  nbValeursPossibles = 0):
        self.i = i
        self.j = j
        self.nbValeursPossibles = nbValeursPossibles


#global variable
existeSurLigne = [ [False]*9 for i in range(9)]
existeSurColonne = [ [False]*9 for i in range(9)]
existeSurBloc = [ [False]*9 for i in range(9)]

def solve_back(sudoku):

    resolution(sudoku.area)


def estValide(grille, position):

    if position is None:
        return True

    i = position.i
    j = position.j

    for k in range(9):
        if not(existeSurLigne[i][k]) and not(existeSurColonne[j][k]) and not(existeSurBloc[3*int((i/3))+int((j/3))][k]):
            existeSurLigne[i][k] = existeSurColonne[j][k] = existeSurBloc[3*int((i/3))+int((j/3))][k] = True

            if estValide(grille, position.next()):
                grille[i][j] = k+1
                return True

            existeSurLigne[i][k] = existeSurColonne[j][k] = existeSurBloc[3*(i/3)+(j/3)][k] = False

    return False


# Calcule le nombre de valeurs possibles pour une case vide
def nb_possibles(i, j):

    ret = 0
    for k in range(9):
        if not(existeSurLigne[i][k]) and not(existeSurColonne[j][k]) and not(existeSurBloc[3*int((i/3))+int((j/3))][k]):
            ret += 1

    return ret


def resolution(grille):

    for i in range(9):
        for j in range(9):
            existeSurLigne[i][j] = existeSurColonne[i][j] = existeSurBloc[i][j] = False

    k = 0
    for i in range(9):
        for j in range(9):
            k = grille[i][j]
            if k != 0:
                existeSurLigne[i][k-1] = existeSurColonne[j][k-1] = existeSurBloc[3*(int(i/3))+int((j/3))][k-1] = True

    positions = []
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                positions.insert(0, Case(i, j, nb_possibles(i, j)))

    positions = sorted(positions, key=lambda Case: Case.nbValeursPossibles)

    ret = estValide(grille, iter(positions).next())

    del positions

    return ret, grille
