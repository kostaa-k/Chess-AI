'''
Created on Feb. 19, 2019

@author: Kosta
'''

class Board():
    
    BoardArray = []
    
    def __init__(self):
        self.BoardArray = [8][8]
        for x in range(0,8):
            for y in range(0,8):
                a_square = Square(x, y)
                self.BoardArray.append(a_square)
        
    
    def getSquare(self, x, y):
        
        return self.BoardArray[x][y]
    
class Square():
    x = 0
    y = 0
    piece = None
    def __init__(self, positionx, positiony, piece = None):
        self.x = positionx
        self.y = positiony
        if (piece is not None):
            self.piece = piece
        else:
            self.piece = None