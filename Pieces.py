'''
Created on 2019 M03 26

@author: kale3370
'''
#from Board import board
import Board
#from Board import board
import tkinter as tk

class piece():
    
    name = ""
    colour = ""
    x = -1
    y = -1
    image = None
    id = -1
    moves = 0

    potentials = []
    total_name = ""
    
    def __init__(self, piece_name, the_colour, pos_x, pos_y, piece_id = -1, the_potentials = []):
        self.name = piece_name
        self.colour = the_colour
        self.x = pos_x
        self.y = pos_y
        self.image = None
        self.total_name = ""
        self.id = piece_id
        self.moves = 0
        
        self.potentials = the_potentials

    def set_potential(self, po):
        for x in po:
            self.potentials.append(x)

    def get_potential(self, board):
        
        potentials = []
        
        if (self.name == "pawn" and self.colour == "white"):
            potentials = white_pawn_potential(self, board)
        elif (self.name == "pawn" and self.colour == "black"):
            potentials = black_pawn_potential(self, board)
        elif(self.name == "rook"):
            potentials = left_right_potential(self, board)
            potentials2 = up_down_potential(self, board)
            
            if(potentials2 is not None):
                for x in potentials2:
                    potentials.append(x)


        elif(self.name == "bishop"):
            potentials = diagonal_potential(self, board)

        elif(self.name == "queen"):
            potentials1 = left_right_potential(self, board)
            potentials2 = up_down_potential(self, board)  
            potentials3 = diagonal_potential(self, board)
            
            if (potentials2 is not None):
                for x in potentials2:
                    potentials1.append(x)
                
            if (potentials3 is not None):
                for x in potentials3:
                    potentials1.append(x)

            if (potentials1 is not None):
                for x in potentials1:
                    potentials.append(x)
                
        elif(self.name == "knight"):
            potentials = knight_potential(self, board)
        elif(self.name == "king"):
            potentials = king_potential(self, board)
            
        return potentials
        
        
        
def rook_potential(the_piece, the_board):
    brd = the_board.board_array
    

def king_potential(the_piece, brd):
    
    x = the_piece.x
    y = the_piece.y
    
    changes_in_x = [-1, 0, 1]
    changes_in_y = [-1, 0, 1]
    
    potential = []
    
    
    for i in changes_in_x:
        if(x+i >= 0 and x+i < 8):
            for p in changes_in_y:
                if(y+p >= 0 and y+p < 8):
                    if(i != 0 and p != 0):
                        temp_piece = brd[x+i][y+p]
                        if(temp_piece.name == ""):
                            potential.append(temp_piece)
                        else:
                            if(temp_piece.colour != the_piece.colour):
                                potential.append(temp_piece)
    
    
    return potential
                
    

def white_pawn_potential(the_piece, brd):
    
    x = the_piece.x
    y = the_piece.y
    can_double = False
    
    if (y == 1):
        can_double = True
    
    potential = []
    
    if (can_double == True):
        temp_piece = brd[x][y+1]
        if(temp_piece.name == ""):
            potential.append(temp_piece)
            temp_piece = brd[x][y+2]
            if(temp_piece.name == ""):
                potential.append(temp_piece)
    
    else:
        temp_piece = brd[x][y+1]
        if(temp_piece.name == ""):
            potential.append(temp_piece)
            
    
    if(x+1 < 8):
        temp_piece = brd[x+1][y+1]
        if(temp_piece.name != ""):
            if(temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
    
    if(x-1 >=0):
        temp_piece = brd[x-1][y+1]
        if(temp_piece.name != ""):
            if(temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                
    return potential


def black_pawn_potential(the_piece, brd):
    
    x = the_piece.x
    y = the_piece.y
    can_double = False
    
    if (y == 6):
        can_double = True
    
    potential = []
    
    if (can_double == True):
        temp_piece = brd[x][y-1]
        if(temp_piece.name == ""):
            potential.append(temp_piece)
            temp_piece = brd[x][y-2]
            if(temp_piece.name == ""):
                potential.append(temp_piece)
    
    else:
        temp_piece = brd[x][y-1]
        if(temp_piece.name == ""):
            potential.append(temp_piece)
    
    if(x+1 < 8):
        temp_piece = brd[x+1][y-1]
        if(temp_piece.name != ""):
            if(temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
    
    if(x-1 >=0):
        temp_piece = brd[x-1][y-1]
        if(temp_piece.name != ""):
            if(temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                
    
    return potential
    

def knight_potential(the_piece, brd):

    change_x = [-2, -2, -1, -1, 1, 1, 2, 2]
    change_y = [-1, 1, -2, 2, -2, 2, -1, 1]
    
    
    potential = []
    
    x = the_piece.x
    y = the_piece.y
    
    for i in range(0, len(change_x)):
        chg_x = change_x[i]
        chg_y = change_y[i]
        
        new_pos_x = chg_x+x
        new_pos_y = chg_y+y 
        
        if (new_pos_x>=0 and new_pos_x<8 and new_pos_y>=0 and new_pos_y<8):
            
            temp_piece = brd[new_pos_x][new_pos_y]
            
            if (temp_piece.name == ""):
                potential.append(temp_piece)
            else:
                if (temp_piece.colour != the_piece.colour):
                    potential.append(temp_piece)
                    
                    
    return potential
        

def diagonal_potential(the_piece, brd):
    
    x = the_piece.x
    y = the_piece.y
    potential = []
    
    
    
    blocked = 0
    count = 1
    while(blocked == 0 and (x+count) < 8 and (y+count) < 8):
        temp_piece = brd[x+count][y+count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
        
        
    blocked = 0
    count = 1
    while(blocked == 0 and (x+count) < 8 and (y-count) >= 0):
        temp_piece = brd[x+count][y-count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
        
        
    blocked = 0
    count = 1
    while(blocked == 0 and (x-count) >=0 and (y+count) < 8):
        temp_piece = brd[x-count][y+count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
        
        
    blocked = 0
    count = 1
    while(blocked == 0 and (x-count) >= 0 and (y-count) >= 0):
        temp_piece = brd[x-count][y-count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1


    return potential


def left_right_potential(the_piece, brd):
    x = the_piece.x
    y = the_piece.y
    potential = []
    
    
    #Go Right
    blocked = 1
    count = 1
    while(blocked == 0 and (x+count) < 8):
        temp_piece = brd[x+count][y]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
        
        
    blocked = 1
    count = 1
    while(blocked == 0 and (x-count) >= 0):
        temp_piece = brd[x-count][y]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
        
    return potential
    
    
def up_down_potential(the_piece, brd):

    x = the_piece.x
    y = the_piece.y    

    potential = []
    
    blocked = 0
    count = 1
    while(blocked == 0 and (y+count) < 8):
        temp_piece = brd[x][y+count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
                break
            else:
                blocked = 1
                break
                
        count = count+1
                
    blocked = 0
    count = 1      
    while(blocked == 0 and (y-count) >=0):
        temp_piece = brd[x][y-count]
        if (temp_piece.name == ""):
            potential.append(temp_piece)
        else:
            if (temp_piece.colour != the_piece.colour):
                potential.append(temp_piece)
                blocked = 1
            else:
                blocked = 1
                break
            
        count = count+1
    
    return potential
                
                

def print_potentials(the_potentials, the_piece):
    
    if (the_potentials is not None):
        if (len(the_potentials)> 0):
            print(the_piece.name+" : ", end = "")
            for x in the_potentials:
                pos_string = Board.convert_spot(x)
                print(pos_string+" ", end = "")
        
            print()
