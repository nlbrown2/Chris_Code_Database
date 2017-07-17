def move_executor(board, my_color, opposite_color, strategy, print_bool):

    from calculate_legal_moves import calculate_legal_moves
    from strategy_executor import strategy_executor

    try:
        [net_legal_moves, net_scores, net_capture_scores, player_move, legal_moves_index, score_index] = calculate_legal_moves(board, my_color, opposite_color, strategy, print_bool)
    except:
        #print("either no legal moves or problem with calculate_legal_moves")
        return [-100]
    location_to_place = strategy_executor(strategy, net_legal_moves, net_scores, print_bool, net_capture_scores, player_move)
    if print_bool == 1:
        print('Chosen location: ', location_to_place)
    i = location_to_place[0]
    j = location_to_place[1]

    # Right
    if location_to_place in legal_moves_index[0]: #if squares to the right need to be flipped
        number_of_flips = score_index[0][legal_moves_index[0].index(location_to_place)] #find the previously calculated score in the right direction for this move
        for k in range(number_of_flips+1): #flip the location square and all of the ones to the right of it until we reach the score that was previously calculated
            board[i,j+k] = my_color

    # Left
    if location_to_place in legal_moves_index[1]:
        number_of_flips = score_index[1][legal_moves_index[1].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i,j-k] = my_color

    # Up
    if location_to_place in legal_moves_index[2]:
        number_of_flips = score_index[2][legal_moves_index[2].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i-k, j] = my_color

    # Down
    if location_to_place in legal_moves_index[3]:
        number_of_flips = score_index[3][legal_moves_index[3].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i+k, j] = my_color

    # Up Right
    if location_to_place in legal_moves_index[4]:
        number_of_flips = score_index[4][legal_moves_index[4].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i-k, j+k] = my_color

    # Up Left
    if location_to_place in legal_moves_index[5]:
        number_of_flips = score_index[5][legal_moves_index[5].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i-k, j-k] = my_color

    # Down Right
    if location_to_place in legal_moves_index[6]:
        number_of_flips = score_index[6][legal_moves_index[6].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i+k, j+k] = my_color

    # Down Left
    if location_to_place in legal_moves_index[7]:
        number_of_flips = score_index[7][legal_moves_index[7].index(location_to_place)]
        for k in range(number_of_flips+1):
            board[i+k, j-k] = my_color

    return board
