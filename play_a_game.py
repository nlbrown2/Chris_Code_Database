def play_a_game(board, print_bool, black_input, white_input, display_on_lights_boolean):

    ## Runs through a game, calling the Black_move and White_move functinos to make moves, then updates the weight grid using the update_weight_grid function
    
    import random
    from Black_and_white_moves import Black_Move
    from Black_and_white_moves import White_Move
    from update_weight_grid import update_weight_grid
    from strategy_picker import strategy_picker
    from display_reversi_board_on_lights import display_reversi_board_on_lights

    output_score_black = [2]
    output_score_white = [2]
    end_game_black = 0
    end_game_white = 0

    if display_on_lights_boolean == 1:
        display_reversi_board_on_lights(board)
    for move in range(1, 200):

            ### Chose Strategies ###
            [black_strategy, white_strategy, black_input, white_input] = strategy_picker(move, black_input, white_input)

            #input('\nPress Enter for next move')
            
            if move%2 == 1: #if it's odd
                if print_bool == 1:
                    print('-'*100)
                    print('Move ', move, '. Black\'s Move.')
                    print('-'*100)

                if output_score_black != [-100]:  # the -100 value indicates the end of the game, and there's a bunch of checks to see if the game is over. look at removing this and making an end game function in the future
                    previous_score_black = output_score_black

                output_scores = Black_Move(board, move, black_strategy, print_bool, display_on_lights_boolean)
                #print(output_scores)

                if output_scores != [-100]:
                    output_score_white = output_scores[0]
                    output_score_black = output_scores[1]
                    if print_bool == 1:
                        print('\nBlack\'s Score After Move ', move, ': ', output_score_black)
                        print('White\'s Score After Move ', move, ': ', output_score_white)
                else:
                    end_game_black = 1


            if move%2 == 0: #if it's even

                if print_bool == 1:
                    print('-'*100)
                    print('Move ', move, '. White\'s Move.')
                    print('-'*100)
                if output_score_white != [-100]:
                    previous_score_white = output_score_white
                output_scores = White_Move(board, move, white_strategy, print_bool, display_on_lights_boolean)
                if output_scores != [-100]:
                    output_score_white = output_scores[0]
                    output_score_black = output_scores[1]
                    if print_bool == 1:
                        print('\nBlack\'s Score After Move ', move, ': ', output_score_black)
                        print('White\'s Score After Move ', move, ': ', output_score_white)
                else:
                    end_game_white = 1


            if end_game_black and end_game_white:
                if previous_score_black > previous_score_white:
                    winner = 'black'
                    winning_score = previous_score_black
                if previous_score_black < previous_score_white:
                    winner = 'white'
                    winning_score = previous_score_white
                if previous_score_black == previous_score_white:
                    winner = 'tie'
                    winning_score = previous_score_black
                if print_bool == 1:
                    print('\nGame Over. Winner is ', winner, ' with a score of ', winning_score, ' in ', move-1, ' moves')

                update_weight_grid(board, winner, print_bool)
                break

    return winner
