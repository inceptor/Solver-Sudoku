__author__ = 'Inceptor'

class Sudoku:
    def __init__(self, area = [list(range(1,10))] * 9 ):
        self.area = area

    def print(self):
        for x in range(0, 3):
            for i in range(0,3):
                for y in range(0,3):
                    for j in range(0, 3):
                        print(self.area[3*x+i][3*y+j], end=' ')
                    print('', end='\t')
                print('')
            print('')