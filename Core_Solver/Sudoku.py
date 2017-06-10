__author__ = 'Inceptor'

class Sudoku:
    def __init__(self, area = [list(range(1,10))] * 9 ):
        self.area = area

    def print(self):
        for x in range(0, 3):
            for i in range(0,3):
                for y in range(0,3):
                    for j in range(0, 3):
                        if self.area[3*x+i][3*y+j] is None:
                            print('X', end=' ')
                        else:
                            print(self.area[3*x+i][3*y+j], end=' ')
                    print('', end='\t')
                print('')
            print('')

    def get(self):
        return self.area

    def checkValidity(self):
        return ( self.__checklines() or self.__checkcolumns() or self.__checksquare() )

    def __checklines(self):
        for i in range(0,9):
            sum = 1
            for j in range(0,9):
                sum *= self.area[i][j]
            if sum != 362880: # factorial 9
                return 1
        return 0

    def __checkcolumns(self):
        for i in range(0,9):
            sum = 1
            for j in range(0,9):
                sum *= self.area[j][i]
            if sum != 362880: # factorial 9
                return 1
        return 0

    def __checksquare(self):
        for squareI in range(0,3):
            for squareJ in range(0,3):
                sum = 1
                for i in range(0,3):
                    for j in range(0,3):
                        sum *= self.area[3*squareI+i][3*squareJ+j]
                if sum != 362880: # factorial 9
                    return 1
        return 0
