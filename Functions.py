


def open_single_pgn(filename):

    f = open(filename, mode = "r", encoding = "utf-8")

    all_lines = f.readlines()

    move_count = 0

    pieces = []
    to_xs = []
    to_ys = []
    from_xs = []
    from_ys = []

    for line in all_lines:

        all_moves = line.split(".")

        for i in range(0, len(all_moves)):
            
            move_count = move_count+1

            temp_moves = all_moves[i]

            if(move_count < 20):
                temp_moves = temp_moves[:-1]
            elif(move_count<200):
                temp_moves = temp_moves[:-2]
            elif(move_count<2000):
                temp_moves = temp_moves[:-3]

            if(temp_moves.count(" ") >= 1):
                moves = temp_moves.split(" ")
                for x in range(0, len(moves)-1):
                    piece_moving, to_x, to_y, from_x, from_y = get_move(moves[x], move_count)
                    print(piece_moving, to_x, to_y)
                    pieces.append(piece_moving)
                    to_xs.append(to_x)
                    to_ys.append(to_y)
                    from_xs.append(from_x)
                    from_ys.append(from_y)


    return pieces, to_xs, to_ys, from_xs, from_ys


    return pieces, to_xs, to_ys

def get_move(str_move, move_count):

    to_x = -1
    to_y = -1
    from_x = -1
    from_y = -1
    piece_moving = ""

    print(str_move+" ", end="")

    if(len(str_move) < 2):
        print()
    else:
        if(str_move.istitle() == True):

            if(str_move[0] != "O"):
                piece_moving = get_piece_name(str_move[0])
                
                if(str_move[1] == "x"):
                    spot = str_move[1]+str_move[2]+str_move[3]

                    to_x = get_x_axis(str_move[2])
                    to_y = ((int)(str_move[3]))-1

                else:
                    if(get_x_axis(str_move[1]) != -1):
                        if(get_x_axis(str_move[2]) != -1):
                            from_x = get_x_axis(str_move[1])
                            to_x = get_x_axis(str_move[2])
                            to_y = ((int)(str_move[3]))-1
                        else:
                            to_x = get_x_axis(str_move[1])
                            to_y = ((int)(str_move[2]))-1

                    else:
                        from_y = ((int)(str_move[1]))-1
                        if(str_move[2] == "x"):
                            to_x = get_x_axis(str_move[3])
                            to_y = ((int)(str_move[4]))-1
                        else:
                            to_x = get_x_axis(str_move[2])
                            to_y = ((int)(str_move[3]))-1

            else:
                piece_moving = "king"
                if(str_move == "O-O"):
                    to_x = 6
                    if(move_count%2 == 0):
                        to_y = 7
                    else:
                        to_y = 0
                else:
                    to_x = 2
                    if(move_count%2 == 0):
                        to_y = 7
                    else:
                        to_y = 0



        else:
            piece_moving = "pawn"
            if(str_move[1] == "x"):
                from_x = get_x_axis(str_move[0])
                to_x = get_x_axis(str_move[2])
                to_y = ((int)(str_move[3]))-1
            else:
                to_x = get_x_axis(str_move[0])
                to_y = ((int)(str_move[1]))-1
    
    return piece_moving, to_x, to_y, from_x, from_y



def get_piece_name(letter):

    piece = ""

    if(letter == "N"):
        piece = "knight"
    elif(letter == "K"):
        piece = "king"
    elif(letter == "Q"):
        piece = "queen"
    elif(letter == "B"):
        piece = "bishop"
    elif(letter == "R"):
        piece = "rook"

    return piece


def get_x_axis(letter):

    abcs = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for i in range(0,8):
        if abcs[i] == letter:
            return i

    return -1