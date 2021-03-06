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
import Functions

#Create Board Array First:

the_board = board()
brd = the_board.get_pieces()
the_board.set_board()


#the_board.print_board()


#TESTING OPENING PGN
pieces, to_xs, to_ys, from_xs, from_ys = Functions.open_single_pgn("example_pgn.txt")


time.sleep(2)
#SET UP GUI BOARD
root = tk.Tk()
gui_board = GameBoard(root)
        
gui_board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        
the_board.set_piece_images() 
gui_board = the_board.set_Gui_Board(gui_board, root)
        
        
time.sleep(1)

move_counter = 1
while(move_counter < 50):
    #the_board.make_random_move(move_counter, gui_board)
    the_board.make_pgn_move(move_counter, gui_board, pieces[move_counter-1], to_xs[move_counter-1], to_ys[move_counter-1])
    root.update()
    move_counter = move_counter+1
    the_board.print_board()
    time.sleep(1)


root.mainloop()