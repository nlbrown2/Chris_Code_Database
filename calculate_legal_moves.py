def calculate_legal_moves(board, my_color, opposite_color, strategy, print_bool):
    import math
    from strategy_executor import strategy_executor as strat
    import numpy as np
    weight_grid = np.load('weight_grid.npy')
    
    legal_moves_right = []
    legal_moves_left = []
    legal_moves_up = []
    legal_moves_down = []
    legal_moves_up_right = []
    legal_moves_up_left = []
    legal_moves_down_right = []
    legal_moves_down_left = []

    score_right = []
    score_left = []
    score_up = []
    score_down = []
    score_up_right = []
    score_up_left = []
    score_down_right = []
    score_down_left = []

    capture_score_right = []
    capture_score_left = []
    capture_score_up = []
    capture_score_down = []
    capture_score_up_right = []
    capture_score_up_left = []
    capture_score_down_right = []
    capture_score_down_left = []

    player_move = []
    

    
    for i in range(8): #iterate rows
        for j in range(8): #iterate columns
            if board[i,j] == 0: #if it's empty

                score = 0
                capture_score = 0
                for k in range(j,8):
                    right_square = board[i, k]
                    if right_square == opposite_color: #for black's move, if it's white
                        score += 1
                        capture_score += weight_grid[i,k]
                    if right_square == 0 and k != j:
                        break
                    if right_square == my_color:
                        if k != j+1: #black and not adjacent
                            legal_moves_right.append([i,j])
                            score_right.append(score)
                            capture_score_right.append(capture_score)
                            break
                        else: #immediately breaks in case there are consecutive 2's and it just skips over the first and catches the second
                            break
                
                score = 0
                capture_score = 0
                for k in range(j,-1,-1):
                    left_square = board[i, k]
                    if left_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[i,k]
                    if left_square == 0 and k != j:
                        break
                    if left_square == my_color:
                        if k != j-1:
                            legal_moves_left.append([i,j])
                            score_left.append(score)
                            capture_score_left.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(i, -1, -1):
                    up_square = board[k, j]
                    if up_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[k,j]
                        #up_log.append([i,j])
                    if up_square == 0 and k != i:
                        break
                    if up_square == my_color:
                        if k != i-1:
                            legal_moves_up.append([i,j])
                            score_up.append(score)
                            capture_score_up.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(i, 8):
                    down_square = board[k, j]
                    if down_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[k,j]
                    if down_square == 0 and k != i:
                        break
                    if down_square == my_color:
                        if k != i+1:
                            legal_moves_down.append([i,j])
                            score_down.append(score)
                            capture_score_down.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(0, 7 - max(i,j)+1):
                    down_right_square = board[i+k, j+k]
                    if down_right_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[i+k, j+k]
                    if down_right_square == 0 and k != 0:
                        break
                    if down_right_square == my_color:
                        if k != 1:
                            legal_moves_down_right.append([i,j])
                            score_down_right.append(score)
                            capture_score_down_right.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(0, min(i,j)+1):
                    up_left_square = board[i-k, j-k]
                    if up_left_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[i-k, j-k]
                    if up_left_square == 0 and k != 0:
                        break
                    if up_left_square == my_color:
                        if k != 1:
                            legal_moves_up_left.append([i,j])
                            score_up_left.append(score)
                            capture_score_up_left.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(0, min(i, 7-j)+1):
                    up_right_square = board[i-k, j+k]
                    if up_right_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[i-k, j+k]
                    if up_right_square == 0 and k != 0:
                        break
                    if up_right_square == my_color:
                        if k != 1:
                            legal_moves_up_right.append([i,j])
                            score_up_right.append(score)
                            capture_score_up_right.append(capture_score)
                            break
                        else:
                            break

                score = 0
                capture_score = 0
                for k in range(0, min(7-i, j)+1):
                    down_left_square = board[i+k, j-k]
                    if down_left_square == opposite_color:
                        score += 1
                        capture_score += weight_grid[i+k, j-k]
                    if down_left_square == 0 and k != 0:
                        break
                    if down_left_square == my_color:
                        if k != 1:
                            legal_moves_down_left.append([i,j])
                            score_down_left.append(score)
                            capture_score_down_left.append(capture_score)
                            break
                        else:
                            break

    all_legal_moves = legal_moves_right + legal_moves_left + legal_moves_up + legal_moves_down + legal_moves_up_right + legal_moves_up_left + legal_moves_down_right + legal_moves_down_left
    legal_move_index = [legal_moves_right, legal_moves_left, legal_moves_up, legal_moves_down, legal_moves_up_right, legal_moves_up_left, legal_moves_down_right, legal_moves_down_left]
    all_scores = score_right + score_left + score_up + score_down + score_up_right + score_up_left + score_down_right + score_down_left
    score_index = [score_right, score_left, score_up, score_down, score_up_right, score_up_left, score_down_right, score_down_left]
    all_capture_scores = capture_score_right + capture_score_left + capture_score_up + capture_score_down + capture_score_up_right + capture_score_up_left + capture_score_down_right + capture_score_down_left

    if all_legal_moves == []:
        if print_bool == 1:
            print('No more possible moves') #End Game condition
        return [-100]

    copy_all_legal_moves = []
    for item in all_legal_moves: #Because setting two lists equal to each other seems to link them so popping one pops the other
        copy_all_legal_moves.append(item)

    copy_all_scores = []
    for item in all_scores:
        copy_all_scores.append(item)

    copy_all_capture_scores = []
    for item in all_capture_scores:
        copy_all_capture_scores.append(item)

    #print(copy_all_scores)
    net_legal_moves = []
    net_scores = []
    net_capture_scores = []
    while len(copy_all_legal_moves) != 0: #In this section, I cycle through all of the legal moves and add up all of the scores for that index. The moves are stored in net_legal_moves, and the corresponding scores are in net_scores
        net_legal_moves.append(copy_all_legal_moves[0])
        temp_scores_sum = copy_all_scores[0]
        temp_capture_scores_sum = copy_all_capture_scores[0]
        for test_index in range(len(copy_all_legal_moves)-1, 0, -1):
            if copy_all_legal_moves[test_index] == copy_all_legal_moves[0]:
                temp_scores_sum += copy_all_scores[test_index]
                temp_capture_scores_sum += copy_all_capture_scores[test_index]
                copy_all_legal_moves.pop(test_index)
                copy_all_scores.pop(test_index)
                copy_all_capture_scores.pop(test_index)
        net_scores.append(temp_scores_sum)
        net_capture_scores.append(temp_capture_scores_sum)
        copy_all_legal_moves.pop(0)
        copy_all_scores.pop(0)
        copy_all_capture_scores.pop(0)

    if print_bool == 1:
        print('Legal Moves: ', net_legal_moves)
        print('Corresponding Scores: ', net_scores)
        print('Strategy: ', strategy)

    if strategy == 'human_player':  #Get a move input from the user. Lots of code to make sure the user inputs in the form I want

        player_move_index_1 = 'just a starter string'
        player_move_index_2 = 'to make the while loop work'

        while player_move_index_1 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            player_move_index_1 = input('Where would you like to move (index 1)? >> ')
            if player_move_index_1 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                print('Sorry, invalid input. Please try again')
        while player_move_index_2 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            player_move_index_2 = input('Where would you like to move (index 2)? >> ')
            if player_move_index_2 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                print('Sorry, invalid input. Please try again')

        player_move = [ord(player_move_index_1)-48, ord(player_move_index_2)-48]

        while 1:
            if player_move in net_legal_moves:
                break
            else:
                print('Sorry, invalid move.')
                player_move_index_1 = 'just a starter string'
                player_move_index_2 = 'to make the while loop work'
                while player_move_index_1 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    player_move_index_1 = input('Try again (index 1)? >> ')
                    if player_move_index_1 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                        print('Sorry, invalid input. Please try again')
                while player_move_index_2 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    player_move_index_2 = input('Try again (index 2)? >> ')
                    if player_move_index_2 not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                        print('Sorry, invalid input. Please try again')

                player_move = [ord(player_move_index_1)-48, ord(player_move_index_2)-48] 

    return [net_legal_moves, net_scores, net_capture_scores, player_move, legal_move_index, score_index]
