__author__ = 'Inceptor'

from Core_Solver.Sudoku import *
from Core_Solver.basic_perso_algo import *

def testCheckCorrectSudoku():
    test = Sudoku([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]])

    assert test.checkValidity() == 0

def testCheckIncorrectSudoku():
    test  = Sudoku( [ [i for i in range(1,10)] for j in range(9)] ) #Bad columns
    test2 = Sudoku( [ [j for i in range(9)] for j in range(1,10)] ) #Bad line
    test3 = Sudoku( [ [ (j+i)%9+1 for i in range(1,10)] for j in range(9)] ) #Bad square

    assert test.checkValidity() and test2.checkValidity() and test3.checkValidity() == 1 #Bad columns and line and square


def testSolverEasy():
    test = Sudoku([[6,8,5,2,1,0,4,7,0],[4,1,0,3,0,8,2,9,0],[0,2,3,5,0,0,0,0,6],[0,4,0,7,2,6,9,3,0],[0,6,1,8,9,3,7,5,4],[0,3,0,1,0,0,0,8,0],[0,7,2,4,5,1,3,6,9],[0,0,0,0,8,0,1,0,0],[0,9,0,0,0,7,5,2,0]]) #easy easy sudoku to solve
    test = solve_Perso(test)
    solution = Sudoku([[6,8,5,2,1,9,4,7,3],[4,1,7,3,6,8,2,9,5],[9,2,3,5,7,4,8,1,6],[5,4,8,7,2,6,9,3,1],[2,6,1,8,9,3,7,5,4],[7,3,9,1,4,5,6,8,2],[8,7,2,4,5,1,3,6,9],[3,5,6,9,8,2,1,4,7],[1,9,4,6,3,7,5,2,8]])
    assert test.get() == solution.get() and test.checkValidity() == 0

def testSolverMedium():
    test = Sudoku([[4,0,7,3,0,6,0,0,0],[0,0,0,0,0,0,0,0,0],[3,0,5,2,9,4,0,0,0],[0,6,3,7,0,1,0,2,0],[7,0,2,0,3,0,8,4,0],[0,0,9,0,8,0,0,0,0],[9,3,4,0,0,0,0,5,0],[0,1,8,0,0,0,0,0,6],[0,0,0,0,5,0,1,0,0]]) #medium
    test = solve_Perso(test)
    solution = Sudoku([[4,9,7,3,1,6,5,8,2],[6,2,1,8,7,5,3,9,4],[3,8,5,2,9,4,6,1,7],[8,6,3,7,4,1,9,2,5],[7,5,2,6,3,9,8,4,1],[1,4,9,5,8,2,7,6,3],[9,3,4,1,6,7,2,5,8],[5,1,8,9,2,3,4,7,6],[2,7,6,4,5,8,1,3,9]])
    assert test.get() == solution.get() and test.checkValidity() == 0

def testSolverHard():
    test = Sudoku([[0,0,7,5,0,3,4,6,0],[0,0,0,6,0,1,9,2,0],[0,0,0,0,4,0,5,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,7,6,2,0,8,0],[0,2,0,0,1,9,0,4,0],[9,0,6,0,2,0,0,0,7],[3,0,1,0,0,0,0,0,0],[0,7,0,0,0,0,0,1,0]]) #hard
    test = solve_Perso(test)
    solution = Sudoku([[2,1,7,5,9,3,4,6,8],[8,5,4,6,7,1,9,2,3],[6,9,3,2,4,8,5,7,1],[1,6,9,4,8,5,7,3,2],[4,3,5,7,6,2,1,8,9],[7,2,8,3,1,9,6,4,5],[9,8,6,1,2,4,3,5,7],[3,4,1,8,5,7,2,9,6],[5,7,2,9,3,6,8,1,4]])
    #assert test.get() == solution.get() and test.checkValidity() == 0
    pass

def testSolverVeryHard():
     test = Sudoku([[0,0,0,0,0,1,0,0,0],[7,0,6,5,8,0,0,0,4],[0,2,0,0,0,6,0,3,0],[0,3,0,0,4,0,0,5,0],[4,0,2,0,0,0,7,0,3],[0,1,0,0,3,0,0,0,0],[0,8,0,1,0,0,0,9,0],[1,0,0,0,2,0,6,0,5],[0,0,0,7,0,0,0,0,0]]) #hard
     test = solve_Perso(test)
     solution = Sudoku([[3,4,8,2,9,1,5,7,6],[7,9,6,5,8,3,1,2,4],[5,2,1,4,7,6,8,3,9],[8,3,7,6,4,2,9,5,1],[4,6,2,9,1,5,7,8,3],[9,1,5,8,3,7,4,6,2],[6,8,3,1,5,4,2,9,7],[1,7,9,3,2,8,6,4,5],[2,5,4,7,6,9,3,1,8]])
     #assert test.get() == solution.get() and test.checkValidity() == 0
     pass
