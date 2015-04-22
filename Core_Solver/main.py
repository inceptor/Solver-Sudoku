__author__ = 'Inceptor'

from Sudoku import *
from basic_perso_algo import *

test = Sudoku([[6,8,5,2,1,0,4,7,0],[4,1,0,3,0,8,2,9,0],[0,2,3,5,0,0,0,0,6],[0,4,0,7,2,6,9,3,0],[0,6,1,8,9,3,7,5,4],[0,3,0,1,0,0,0,8,0],[0,7,2,4,5,1,3,6,9],[0,0,0,0,8,0,1,0,0],[0,9,0,0,0,7,5,2,0]])
test.print()
test = solve_Perso(test)
test.print()