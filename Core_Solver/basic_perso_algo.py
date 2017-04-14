__author__ = 'Inceptor'

import copy

'''
Goal :
4 steps.
 step 1 : duplicate the grid and change the type (boolean). Make true the case if there are empty.
 step 2 : we begin with the number 1. pick, if existe,  the number on the grid. Create a tempory grid (boolean) who
            is the duplication of the precedent boolean grid. switch true on false (it's mean : the case is impossible
            to contain the number selected) if the case is on the vertical and horizontal of the number picked and lock
            the sub-grid (turn in on False). Do it for all ocurance of the number selected.
 step 3 : Do the step 2 for all number (1,2,3,4,5,6,7,8,9).
 step 4 : If the sudoku is not complited, retry the step 2..
 '''

class Case:
    def __init__(self, number = 0, i = -1, j = -1 ):
        self.i = i
        self.j = j
        self.number = number

def solve_Perso(sudoku):

    #Initialisation /step 1
    boolSudoku = [ [True] * 9 for i in range(9)]
    allCase = [[] for i in range(9)] #Contains all well-know numbers. 1D = Number, 2D = list of this number

    for i in range(9):
        for j in range(9):
            if sudoku.area[i][j] != 0:
                boolSudoku[i][j] = False
                allCase[sudoku.area[i][j]-1].append(Case(sudoku.area[i][j],i,j))

    #the begin
    found = True
    while found:
        found = False
        for n in range(1,10):
            boolSudokuTemp = copy.deepcopy(boolSudoku)
            #Optimisation begin here
            for c in range(len(allCase[n-1])): # all number concern
                for x in range(9):
                    boolSudokuTemp[x][allCase[n-1][c].j] = False
                for y in range(9):
                    boolSudokuTemp[allCase[n-1][c].i][y] = False
                #lock the sub-grid
                corI = int(allCase[n-1][c].i / 3)
                corJ = int(allCase[n-1][c].j / 3)
                for x in range(3):
                    for y in range(3):
                        boolSudokuTemp[3*corI + x][3*corJ + y] = False

            #Check the free case
            for i in range(3):
                for j in range(3):
                    nbCaseLib = 0

                    for x in range(3):
                        for y in range(3):
                            if boolSudokuTemp[3*i + x][3*j + y] == True:
                                nbCaseLib += 1
                                corI = 3*i + x
                                corJ = 3*j + y


                    if nbCaseLib == 1:
                        sudoku.area[corI][corJ] = n
                        boolSudoku[corI][corJ] = False
                        allCase[n-1].append(Case(n,corI,corJ))
                        found = True

    print("\nSolution Done !\n")

    return sudoku