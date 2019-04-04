'''
Created on 2019 M03 26

@author: kale3370
'''
from Pieces import piece
import tkinter as tk
import Gui_Board
from Gui_Board import GameBoard
import time
from copy import copy, deepcopy
import math
import random

class board:
    
    board_array = [[0 for x in range(8)] for y in range(8)] 
    
    
    
    def __init__(self):
        
        counter = 0
        for x in range(0, 8):
            for i in range(0,8):
                temp = piece("", "", x, i, counter)
                self.board_array[x][i] = temp
                counter = counter+1
                
    
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
                    
                    
        
    def print_board(self):
        
        for y in range(0,8):
            for x in range(0,8):
                temp_piece = self.board_array[x][7-y]
                
                if (temp_piece.name != ""):
                    print(temp_piece.name[:1], " ",  end = "")
                else:
                    print("-  ", end ="")
                
            print()

        print()
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
            
        #gui_board.move_a_piece(the_piece, pos_x, pos_y)
        
        temp = piece("", "", the_piece.x, the_piece.y)
        self.board_array[the_piece.x][the_piece.y] = temp

        the_piece.x = pos_x
        the_piece.y = pos_y
        the_piece.moves = the_piece.moves+1
        self.board_array[pos_x][pos_y] = the_piece


    def white_castling(self):

        #King Side:
        brd = self.board_array
        
        in_check = is_white_in_check(brd)
        
        kingside = 0
        queenside = 0

        #Check if white is in check
        if(in_check == True):
            return 0, 0
        else:
            #Check if king has moved
            if(brd[4][0].name == "king" and brd[4][0].moves == 0):

                #Check rook1 is in right place and hasn't moved - Queen side
                rook1 = brd[0][0]
                if(rook1 == "rook" and rook1.moves == 0):
                    if(brd[1][0].name == "" and brd[2][0].name == "" and brd[3][0].name == ""):
                        black_potentials = get_black_potentials(self)
                        for x in black_potentials:
                            for i in x.potentials:
                                if(i.y == 0):
                                    if(i.x >= 0 or i.x <= 4):
                                        queenside = 1
                
                #Check rook 2 is in the right place and hasn't moved - King side
                rook2 = brd[7][0]
                if(rook2 == "rook" and rook1.moves == 0):
                    if(brd[6][0].name == "" and brd[5][0].name == ""):
                        black_potentials = get_black_potentials(self)
                        for x in black_potentials:
                            for i in x.potentials:
                                if(i.y == 0):
                                    if(i.x >= 4 or i.x <= 7):
                                        kingside = 1

        
        return kingside, queenside



    def black_castling(self):

        #King Side:
        brd = self.board_array
        
        in_check = is_black_in_check(brd)
        
        kingside = 0
        queenside = 0

        #Check if white is in check
        if(in_check == True):
            return 0, 0
        else:
            #Check if king has moved
            if(brd[4][7].name == "king" and brd[4][7].moves == 0):

                #Check rook1 is in right place and hasn't moved - Queen side
                rook1 = brd[0][7]
                if(rook1 == "rook" and rook1.moves == 0):
                    if(brd[1][7].name == "" and brd[2][7].name == "" and brd[3][7].name == ""):
                        white_potentials = get_white_potentials(self)
                        for x in white_potentials:
                            for i in x.potentials:
                                if(i.y == 7):
                                    if(i.x >= 0 or i.x <= 4):
                                        queenside = 1
                
                #Check rook 2 is in the right place and hasn't moved - King side
                rook2 = brd[7][7]
                if(rook2 == "rook" and rook1.moves == 0):
                    if(brd[6][7].name == "" and brd[5][7].name == ""):
                        white_potentials = get_white_potentials(self)
                        for x in white_potentials:
                            for i in x.potentials:
                                if(i.y == 7):
                                    if(i.x >= 4 or i.x <= 7):
                                        kingside = 1
        
        return kingside, queenside
        

    def get_white_potentials(self):

        brd_array = self.board_array

        pieces_that_can_move = []

        for x in range(0,8):
            for y in range(0,8):
                self.board_array[x][y].potentials = []
                temp_piece = brd_array[x][y]
                temp_piece.potentials.clear()
                if(temp_piece.colour == "white"):

                    #print(temp_piece.name, temp_piece.x, temp_piece.y)
                    potential = temp_piece.get_potential(brd_array)

                    if(potential is not None):

                        if(temp_piece.name == "king" and temp_piece.moves == 0):
                            castling = self.white_castling()

                        can_move = 0
                        a_temp_array = []
                        for p in potential:
                            is_legal = is_move_legal(brd_array, temp_piece, p.x, p.y)
                            #print(temp_piece.name, p.x, p.y)
                            if(is_legal == True):
                                #if(temp_piece.name == "bishop"):
                                    #print(temp_piece.name, temp_piece.x, temp_piece.y)
                                can_move = 1
                                a_temp_array.append(p)

                        if(can_move == 1):
                            temp_piece.set_potential(a_temp_array)
                            new_piece = piece(temp_piece.name, temp_piece.colour, temp_piece.x, temp_piece.y, temp_piece.id, a_temp_array)
                            pieces_that_can_move.append(new_piece)

        return pieces_that_can_move


    def get_black_potentials(self):

        brd_array = self.board_array

        pieces_that_can_move = []

        for x in range(0,8):
            for y in range(0,8):
                self.board_array[x][y].potentials = []
                temp_piece = brd_array[x][y]
                temp_piece.potentials.clear()
                if(temp_piece.colour == "black"):
                    potential = temp_piece.get_potential(brd_array)

                    if(potential is not None):
                        can_move = 0
                        a_temp_array = []
                        for p in potential:
                            #print(temp_piece.name, p.x, p.y)
                            is_legal = is_move_legal(brd_array, temp_piece, p.x, p.y)
                            #print(temp_piece.name, p.x, p.y)
                            if(is_legal == True):
                                can_move = 1
                                a_temp_array.append(p)

                        if(can_move == 1):
                            temp_piece.set_potential(a_temp_array)
                            new_piece = piece(temp_piece.name, temp_piece.colour, temp_piece.x, temp_piece.y, temp_piece.id, a_temp_array)
                            pieces_that_can_move.append(new_piece)

        
        king_side, queen_side = self.black_castling()

        if(king_side == 1):
            print("KING SIDE")
        if(queen_side == 1):
            print("QUEEN SIDE")

        return pieces_that_can_move


    def get_a_piece(self, piece_id):

        the_brd = self.board_array

        for x in range(0, 8):
            for y in range(0, 8):
                temp_piece = the_brd[x][y]
                if(temp_piece.id == piece_id):
                    return temp_piece

        
        return None


    def make_random_move(self, move_counter, gui_board):

        if(move_counter %2 == 0):
            #MEANS ITS BLACK's Turn
            movable = self.get_black_potentials()


            total_count = 0

            for i in movable:
                for p in i.potentials:
                    total_count = total_count+1

            random_index = random.randint(1,total_count)

            real_count = 0
            for i in movable:
                for p in i.potentials:
                    real_count = real_count+1
                    if(real_count == random_index):
                        piece_moving = i
                        move_to = p
            

            #and the move will beee:

            the_piece_moving = self.get_a_piece(piece_moving.id)

            self.move_piece(the_piece_moving, move_to.x, move_to.y)

            #print(the_piece_moving.name, move_to.x, move_to.y)

            gui_board.move_a_piece(the_piece_moving, move_to.x, move_to.y , self.board_array)
        
        else:
            movable = self.get_white_potentials()
            
            total_count = 0

            for i in movable:
                for p in i.potentials:
                    total_count = total_count+1

            random_index = random.randint(1,total_count)

            real_count = 0
            for i in movable:
                for p in i.potentials:
                    real_count = real_count+1
                    if(real_count == random_index):
                        piece_moving = i
                        move_to = p

            #and the move will beee:

            the_piece_moving = self.get_a_piece(piece_moving.id)

            self.move_piece(the_piece_moving, move_to.x, move_to.y)

            #print(the_piece_moving.name, move_to.x, move_to.y)

            gui_board.move_a_piece(the_piece_moving, move_to.x, move_to.y , self.board_array)








def is_white_in_check(brd):


    for i in range(0, 8):
        for j in range(0, 8):
            temp_piece = brd[i][j]
            if(temp_piece.colour == "black"):
                #print(temp_piece.colour+" - "+temp_piece.name)
                potentials = temp_piece.get_potential(brd)
                
                if (potentials is not None):
                    for x in potentials:
                        if(x.name == "king" and x.colour == "white"):
                            return True
    
    return False


def is_black_in_check(brd):
    
    for i in range(0, 8):
        for j in range(0, 8):
            temp_piece = brd[i][j]
            if(temp_piece.colour == "white"):
                #print(temp_piece.colour+" - "+temp_piece.name)
                potentials = temp_piece.get_potential(brd)
                
                if (potentials is not None):
                    for x in potentials:
                        if(x.name == "king" and x.colour == "black"):
                            return True
    
    return False

            
def convert_spot(the_piece):
    x = the_piece.x
    y = the_piece.y+1
    
    alphas = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    letter = alphas[x]
    
    position_string = letter+(str)(y)
    
    return position_string




def is_move_legal(old_array, the_piece, pos_x, pos_y):
            
    colour_move = the_piece.colour

    temp = piece("", "", the_piece.x, the_piece.y)

    temp_array = old_array

    old_x = the_piece.x
    old_y = the_piece.y


    a_temp_piece = temp_array[pos_x][pos_y]

    temp_array[pos_x][pos_y] = the_piece
    temp_array[the_piece.x][the_piece.y] = temp


    if (colour_move == "white"):
        is_check = is_white_in_check(temp_array)
    else:
        is_check = is_black_in_check(temp_array)

    if(is_check == True):
        is_legal = False
    else:
        is_legal = True


    temp_array[pos_x][pos_y] = a_temp_piece
    temp_array[old_x][old_y] = the_piece


    return is_legal
    
    


    