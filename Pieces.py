'''
Created on Feb. 19, 2019

@author: Kosta
'''
import Board
from Board import Square

class Piece(object):
    '''
    classdocs
    '''
    colour = ""
    name = ""
    positionx = 0
    positiony = 0

    def __init__(self, colour, x, y, piece_name):
        '''
        Constructor
        '''
        self.colour = colour
        self.positionx = x
        self.positiony = y
        self.name = piece_name
    
   
            