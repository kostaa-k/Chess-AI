'''
Created on Feb. 19, 2019

@author: Kosta
'''

class Queen(object):
    '''
    classdocs
    '''
    colour = ""
    positionx = 0
    positiony = 0

    def __init__(self, colour, x, y):
        '''
        Constructor
        '''
        self.colour = colour
        self.positionx = x
        self.positiony = y