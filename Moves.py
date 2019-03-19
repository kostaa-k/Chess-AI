'''
Created on Feb. 19, 2019

@author: Kosta
'''
import Board
from Board import Square

def QueenSquares(Queen, theBoard):
    squares = RookSquares(Queen, theBoard)
    
        
    return squares



def BishopSquares(Bishop, theBoard):
    blocked = False
    squares = []
    
    x_pos = Bishop.positionx
    y_pos = Bishop.positiony


    i = 1
    while((x_pos-i)>=0 and (y_pos-i)>=0 and blocked == False):
        temp_square = theBoard.getSquare(x_pos-i, y_pos-i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Bishop.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
        
    blocked = False
    i = 1
    while((x_pos+i)<8 and (y_pos+i)<8 and blocked == False):
        temp_square = theBoard.getSquare(x_pos+i, y_pos+i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Bishop.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
        
        
    blocked = False
    i = 1
    while((x_pos+i)<8 and (y_pos-i)>=0 and blocked == False):
        temp_square = theBoard.getSquare(x_pos+i, y_pos+i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Bishop.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
    blocked = False
    i = 1
    while((x_pos-i)>=0 and (y_pos+i)>=0 and blocked == False):
        temp_square = theBoard.getSquare(x_pos+i, y_pos+i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Bishop.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
    return squares

def RookSquares(Rook, theBoard):
    blocked = False
    squares = []
    
    x_pos = Rook.positionx
    y_pos = Rook.positiony
    i = 1
    while((y_pos+i)<8 and blocked == False):
        temp_square = theBoard.getSquare(x_pos, y_pos+i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Rook.colour):
                squares.append(temp_square)
            blocked = True
        i = i+1
            
    blocked = False
    i = 1
    while((y_pos-i)>=0 and blocked == False):
        temp_square = theBoard.getSquare(x_pos, y_pos-i)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Rook.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1
    
    
    blocked = False
    i = 1
    while((x_pos+i)<8 and blocked == False):
        temp_square = theBoard.getSquare(x_pos+i, y_pos)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Rook.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
    blocked = False
    i = 1
    while((x_pos-i)>=0 and blocked == False):
        temp_square = theBoard.getSquare(x_pos-i, y_pos)
        if(temp_square.piece is None):
            squares.append(temp_square)
        else:
            if(temp_square.piece.colour != Rook.colour):
                squares.append(temp_square)
            blocked = True
            
        i = i+1 
        
    return squares
        