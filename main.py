'''
Created on 2019 M03 26

@author: kale3370
'''
from Board import board
import Board
import Pieces
from Pieces import piece
import tkinter as tk
import Gui_Board
from Gui_Board import GameBoard
import time

#Create Board First:

the_board = board()


#the_board.print_board()

#imagedata = "/Pieces/black_bishop.png"

brd = the_board.get_pieces()
#for x in range(0,8):
    #for y in range(0,8):
        #temp_piece = brd_array[x][y]
        #potential = temp_piece.get_potential(the_board)
        #Pieces.print_potentials(potential, temp_piece)
        

root = tk.Tk()
gui_board = GameBoard(root)
        
gui_board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        
the_board.set_board()
the_board.set_piece_images() 
gui_board = the_board.set_Gui_Board(gui_board, root)
        
        
time.sleep(1)

#gui_board = the_board.set_Gui_Board(gui_board, root)
the_piece_name = brd[0][1].total_name

gui_board.movepiece(the_piece_name, 5, 0)
the_board.move_piece(brd[0][1], 0, 3)
#the_board.set_Gui_Board(gui_board, root)

#MOVE PIECE

root.mainloop()
    