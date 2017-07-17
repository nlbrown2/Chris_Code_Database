## These functions call the actual move function then print some information and tally the scores. Returns a vector total scores = [white_score, black_score]

def Black_Move(board, move, strategy, print_bool, display_on_lights_boolean):
    
    from move_executor import move_executor as my_move
    from display_reversi_board_on_lights import display_reversi_board_on_lights
    my_color = 2
    opposite_color = 1
    board = my_move(board, my_color, opposite_color, strategy, print_bool) #calls the function that selects the move and flips the pieces, refreshes the board  
    #print("Board = ", board)

    if len(board) == 1:
        if board == [-100]:
            return [-100]

    if print_bool == 1:
        print('\nBoard State After Move ', move, ': ')
        print(board)
    white_score = 0     #count the number of pieces to get player scores
    black_score = 0

    for i in range(8): 
        for j in range(8):
            if board[i,j] == 1:
                white_score += 1
            if board[i,j] == 2:
                black_score += 1

    total_scores = [white_score, black_score]
    if display_on_lights_boolean == 1:
        display_reversi_board_on_lights(board)
    return total_scores

def White_Move(board, move, strategy, print_bool, display_on_lights_boolean):
    
    from move_executor import move_executor as my_move
    from display_reversi_board_on_lights import display_reversi_board_on_lights
    my_color = 1
    opposite_color = 2
    board = my_move(board, my_color, opposite_color, strategy, print_bool)

    if len(board) == 1:
        if board == [-100]:
            return [-100]
    if print_bool == 1:
        print('\nBoard State After Move ', move, ': ')
        print(board)
    white_score = 0
    black_score = 0

    for i in range(8):
        for j in range(8):
            if board[i,j] == 1:
                white_score += 1
            if board[i,j] == 2:
                black_score += 1

    total_scores = [white_score, black_score]
    if display_on_lights_boolean == 1:
        display_reversi_board_on_lights(board)
    return total_scores
