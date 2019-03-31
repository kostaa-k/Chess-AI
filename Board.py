'''
Created on 2019 M03 26

@author: kale3370
'''
from Pieces import piece
import tkinter as tk
import Gui_Board
from Gui_Board import GameBoard
import time

class board:
    
    board_array = [[0 for x in range(8)] for y in range(8)] 
    
    
    
    def __init__(self):
        
        for x in range(0, 8):
            for i in range(0,8):
                temp = piece("", "", x, i)
                self.board_array[x][i] = temp
                
                
    
    def set_board(self):
        
        #Setting white pawns
        val = 1
        for i in range(0, 8):
            self.board_array[i][val].name = "pawn"
            self.board_array[i][val].colour = "white" 
        
        #Setting black pawns
        val = 6
        for i in range(0, 8):
            self.board_array[i][val].name = "pawn"
            self.board_array[i][val].colour = "black"
            
        
        #Setting white rooks:
        self.board_array[0][0].name = "rook"
        self.board_array[0][0].colour = "white"
        
        #Setting white rooks:
        self.board_array[7][0].name = "rook"
        self.board_array[7][0].colour = "white"
        
        #Setting black rooks:
        self.board_array[0][7].name = "rook"
        self.board_array[0][7].colour = "black"
        
        #Setting black rooks:
        self.board_array[7][7].name = "rook"
        self.board_array[7][7].colour = "black"
        
        #Setting white knights:
        self.board_array[1][0].name = "knight"
        self.board_array[1][0].colour = "white"
        
        #Setting white knights:
        self.board_array[6][0].name = "knight"
        self.board_array[6][0].colour = "white"
        
        #Setting black knights:
        self.board_array[1][7].name = "knight"
        self.board_array[1][7].colour = "black"
        
        #Setting white knights:
        self.board_array[6][7].name = "knight"
        self.board_array[6][7].colour = "black"
        
        
        #Setting white bishops:
        self.board_array[2][0].name = "bishop"
        self.board_array[2][0].colour = "white"
        
        self.board_array[5][0].name = "bishop"
        self.board_array[5][0].colour = "white"
        
        #Setting black bishops:
        self.board_array[2][7].name = "bishop"
        self.board_array[2][7].colour = "black"
        
        self.board_array[5][7].name = "bishop"
        self.board_array[5][7].colour = "black"
        
        
        
        #Setting white queen:
        self.board_array[3][0].name = "queen"
        self.board_array[3][0].colour = "white"
        
        #Setting black queen
        self.board_array[3][7].name = "queen"
        self.board_array[3][7].colour = "black"
        
        
        
        #Setting white king:
        self.board_array[4][0].name = "king"
        self.board_array[4][0].colour = "white"
        
        #Setting black king:
        self.board_array[4][7].name = "king"
        self.board_array[4][7].colour = "black"
        
        
        
    def set_piece_images(self):  
          
        for x in range(0, 8):
            for y in range(0, 8):
                self.board_array[x][y].x = x
                self.board_array[x][y].y = y
                
                if(self.board_array[x][y].name != ""):
                    piece_string = self.board_array[x][y].colour+"_"+self.board_array[x][y].name+".png"
                    
                    filepath_name = "Pieces/"+piece_string
                    self.board_array[x][y].image = tk.PhotoImage(file=filepath_name)
                    
    
    def is_white_in_check(self):
        
        brd = self.board_array
        
        
        for i in range(0, 8):
            for j in range(0, 8):
                temp_piece = brd[i][j]
                if(temp_piece.colour == "black"):
                    #print(temp_piece.colour+" - "+temp_piece.name)
                    potentials = temp_piece.get_potential(self)
                    
                    if (potentials is not None):
                        for x in potentials:
                            if(x.name == "king" and x.colour == "white"):
                                return True
        
        return False
    
    
    def is_black_in_check(self):
        
        brd = self.board_array
        
        
        for i in range(0, 8):
            for j in range(0, 8):
                temp_piece = brd[i][j]
                if(temp_piece.colour == "white"):
                    #print(temp_piece.colour+" - "+temp_piece.name)
                    potentials = temp_piece.get_potential(self)
                    
                    if (potentials is not None):
                        for x in potentials:
                            if(x.name == "king" and x.colour == "black"):
                                return True
        
        return False
                    
        
    def print_board(self):
        
        for y in range(0,8):
            for x in range(0,8):
                temp_piece = self.board_array[x][y]
                
                if (temp_piece.name != ""):
                    print(temp_piece.name[:1], " ",  end = "")
                else:
                    print("-  ", end ="")
                
            print()
            
    
    def set_Gui_Board(self, gui_board, root):
    
        all_images = []

        brd = self.board_array
        
        gui_board.destroy_some_frame
        
        count1 = 0

        for x in range(0,8):
            for y in range(0,8):
                temp_piece = brd[x][7-y]
                if(temp_piece.name != ""):
                    total_name1 = temp_piece.colour + " " + temp_piece.name + (str)(count1)
                    brd[x][7-y].total_name = total_name1
                    
                    all_images.append(temp_piece.image)
                    
                    gui_board.addpiece(total_name1, temp_piece.image, y,x)
                     
                    root.update()
                
                count1 = count1+1
        
           
        
        return gui_board
    

    
    
    def set_piece(self, a_piece):
        print()
            
            
    def get_pieces(self):
        
        return self.board_array
    
    
    def move_piece(self, the_piece, pos_x, pos_y):
            
        the_total_name = the_piece.total_name
        
        temp = piece("", "", the_piece.x, the_piece.y)
        
        self.board_array[pos_x][pos_y] = the_piece
        
        self.board_array[the_piece.x][the_piece.y] = temp
        
            
            
def convert_spot(the_piece):
    x = the_piece.x
    y = the_piece.y+1
    
    alphas = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    letter = alphas[x]
    
    position_string = letter+(str)(y)
    
    return position_string



    
    
    


    