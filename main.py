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

the_board.set_board()

#the_board.print_board()

#imagedata = "/Pieces/black_bishop.png"

brd = the_board.get_pieces()
#for x in range(0,8):
    #for y in range(0,8):
        #temp_piece = brd_array[x][y]
        #potential = temp_piece.get_potential(the_board)
        #Pieces.print_potentials(potential, temp_piece)
        
        
        
#temp_name = "Pieces/black_rook.png"

root = tk.Tk()
gui_board = GameBoard(root)
        
gui_board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        
for x in range(0,8):
    for y in range(0,8):
        temp_piece = brd[x][y]
         
        if(temp_piece.name != ""):
            total_name = temp_piece.colour + " " + temp_piece.name
            piece_string = temp_piece.colour+"_"+temp_piece.name+".png"
            
            filepath_name = "Pieces/"+piece_string
            the_image = tk.PhotoImage(file=filepath_name)
            gui_board.addpiece(total_name, the_image, x,y)
            
            root.update()
            time.sleep(2)
        
        

#gui_board = the_board.set_Gui_Board(gui_board)

#root.mainloop()