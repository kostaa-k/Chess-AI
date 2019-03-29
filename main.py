'''
Created on 2019 M03 26

@author: kale3370
'''
from Board import board
import Board
import Pieces
from Pieces import piece

#Create Board First:

the_board = board()

the_board.set_board()

the_board.print_board()


brd_array = the_board.get_pieces()
for x in range(0,8):
    for y in range(0,8):
        temp_piece = brd_array[x][y]
        potential = temp_piece.get_potential(the_board)
        Pieces.print_potentials(potential, temp_piece)