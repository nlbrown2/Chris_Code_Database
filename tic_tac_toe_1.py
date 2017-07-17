def play_games(x_play_with_weights_bool, o_play_with_weights_bool, number_of_games, x_win_weighting, o_win_weighting, summary_print_bool, print_bool, print_every_move_bool, display_on_lights_boolean):

    import random
    import time
    import itertools
    import pickle
    import math
    from tic_tac_toe_1 import play_games
    if display_on_lights_boolean == 1:
        import Adafruit_WS2801
        import Adafruit_GPIO.SPI as SPI
        import RPi.GPIO as GPIO
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    except Exception as ex:
        print(ex)
        print("Error Encountered")


    if display_on_lights_boolean == 1:
        PIXEL_COUNT = 160
        PIXEL_CLOCK = 11
        PIXEL_DOUT = 10
        pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT,clk=PIXEL_CLOCK,do=PIXEL_DOUT)
        pixels.clear()
        pixels.show()

    global top_left
    global top_mid
    global top_right
    global mid_left
    global mid_mid
    global mid_right
    global bottom_left
    global bottom_mid
    global bottom_right
    
    top_left = '-'
    top_mid = '-'
    top_right = '-'
    mid_left = '-'
    mid_mid = '-'
    mid_right = '-'
    bottom_left = '-'
    bottom_mid = '-'
    bottom_right = '-'

    global x_play_with_weights
    global o_play_with_weights
    x_play_with_weights = x_play_with_weights_bool
    o_play_with_weights = o_play_with_weights_bool
    load_weight_vectors = x_play_with_weights or o_play_with_weights
    game_count = 0
    winner_list = []


    if load_weight_vectors == True:
        f = open('store.pck1', 'rb')
        g = open('store.pck2', 'rb')
        weight_vectors = pickle.load(f)
        weight_vectors_2 = pickle.load(g)
        f.close()
        g.close()
        
    else:
        weight_vector_1 = [0,0,0,0,0,0,0,0,0]
        weight_vector_3 = [0,0,0,0,0,0,0,0,0]
        weight_vector_5 = [0,0,0,0,0,0,0,0,0]
        weight_vector_7 = [0,0,0,0,0,0,0,0,0]
        weight_vector_9 = [0,0,0,0,0,0,0,0,0]
        weight_vectors = [weight_vector_1, weight_vector_3, weight_vector_5, weight_vector_7, weight_vector_9]

        weight_vector_2 = [0,0,0,0,0,0,0,0,0]
        weight_vector_4 = [0,0,0,0,0,0,0,0,0]
        weight_vector_6 = [0,0,0,0,0,0,0,0,0]
        weight_vector_8 = [0,0,0,0,0,0,0,0,0]
        weight_vector_10 = [0,0,0,0,0,0,0,0,0]
        weight_vectors_2 = [weight_vector_2, weight_vector_4, weight_vector_6, weight_vector_8, weight_vector_10]


    if display_on_lights_boolean == 1:
        line_color = Adafruit_WS2801.RGB_to_color(255,255,50) #yellow
        X_color = Adafruit_WS2801.RGB_to_color(50,50,255) #blue
        O_color = Adafruit_WS2801.RGB_to_color(255,50,50) #red
        win_flash_color = Adafruit_WS2801.RGB_to_color(50,255,50) #green
        draw_flash_color = Adafruit_WS2801.RGB_to_color(255,50,255) #purple/pink

    class Game_Over_Winner(Exception): pass
    class Game_Over_Draw(Exception): pass
    class Execute_Error(Exception): pass

    def update_weight_vectors(x_moves, winner):
        for i in range(len(x_moves)):
            if winner == 'X':
                weight_vectors[i][x_moves[i]-1] = weight_vectors[i][x_moves[i]-1] + x_win_weighting
            if winner == 'O':
                weight_vectors[i][x_moves[i]-1] = weight_vectors[i][x_moves[i]-1] - x_win_weighting

        for i in range(len(o_moves)):
            if winner == 'X':
                weight_vectors_2[i][o_moves[i]-1] = weight_vectors_2[i][o_moves[i]-1] - o_win_weighting
            if winner == 'O':
                weight_vectors_2[i][o_moves[i]-1] = weight_vectors_2[i][o_moves[i]-1] + o_win_weighting
        

    def display_on_lights(moves_list, player):
        for i in range(8):
            pixels.set_pixel(2+(16*i), line_color) #Sets each light in third row to line color
            pixels.set_pixel(5+(16*i), line_color) #Same for 6th row
        for i in range(32,40):
            pixels.set_pixel(i, line_color) #Sets each light in 3rd column to line color
        for i in range(80, 88):
            pixels.set_pixel(i, line_color) #Same for 6th column

        if player == 'X':
            display_color = X_color
        if player == 'O':
            display_color = O_color
            
        for location in moves_list:
            if location == 1:
                pixels.set_pixel(0, display_color)
                pixels.set_pixel(1, display_color)
                pixels.set_pixel(16, display_color)
                pixels.set_pixel(17, display_color)
            if location == 2:
                pixels.set_pixel(48, display_color)
                pixels.set_pixel(49, display_color)
                pixels.set_pixel(64, display_color)
                pixels.set_pixel(65, display_color)
            if location == 3:
                pixels.set_pixel(96, display_color)
                pixels.set_pixel(97, display_color)
                pixels.set_pixel(112, display_color)
                pixels.set_pixel(113, display_color)
            if location == 4:
                pixels.set_pixel(3, display_color)
                pixels.set_pixel(4, display_color)
                pixels.set_pixel(19, display_color)
                pixels.set_pixel(20, display_color)
            if location == 5:
                pixels.set_pixel(51, display_color)
                pixels.set_pixel(52, display_color)
                pixels.set_pixel(67, display_color)
                pixels.set_pixel(68, display_color)
            if location == 6:
                pixels.set_pixel(99, display_color)
                pixels.set_pixel(100, display_color)
                pixels.set_pixel(115, display_color)
                pixels.set_pixel(116, display_color)
            if location == 7:
                pixels.set_pixel(6, display_color)
                pixels.set_pixel(7, display_color)
                pixels.set_pixel(22, display_color)
                pixels.set_pixel(23, display_color)
            if location == 8:
                pixels.set_pixel(54, display_color)
                pixels.set_pixel(55, display_color)
                pixels.set_pixel(70, display_color)
                pixels.set_pixel(71, display_color)
            if location == 9:
                pixels.set_pixel(102, display_color)
                pixels.set_pixel(103, display_color)
                pixels.set_pixel(118, display_color)
                pixels.set_pixel(119, display_color)
        pixels.show()
        time.sleep(0.5)

    def win_flash(flash_list, end_game_state): #Same as function above but it flashes the winning squares

        if display_on_lights_boolean == 0:
            return
        if end_game_state == "win":
            display_color = win_flash_color
        if end_game_state == "draw":
            display_color = draw_flash_color
        
        for location in flash_list:
            if location == 1:
                pixels.set_pixel(0, display_color)
                pixels.set_pixel(1, display_color)
                pixels.set_pixel(16, display_color)
                pixels.set_pixel(17, display_color)
            if location == 2:
                pixels.set_pixel(48, display_color)
                pixels.set_pixel(49, display_color)
                pixels.set_pixel(64, display_color)
                pixels.set_pixel(65, display_color)
            if location == 3:
                pixels.set_pixel(96, display_color)
                pixels.set_pixel(97, display_color)
                pixels.set_pixel(112, display_color)
                pixels.set_pixel(113, display_color)
            if location == 4:
                pixels.set_pixel(3, display_color)
                pixels.set_pixel(4, display_color)
                pixels.set_pixel(19, display_color)
                pixels.set_pixel(20, display_color)
            if location == 5:
                pixels.set_pixel(51, display_color)
                pixels.set_pixel(52, display_color)
                pixels.set_pixel(67, display_color)
                pixels.set_pixel(68, display_color)
            if location == 6:
                pixels.set_pixel(99, display_color)
                pixels.set_pixel(100, display_color)
                pixels.set_pixel(115, display_color)
                pixels.set_pixel(116, display_color)
            if location == 7:
                pixels.set_pixel(6, display_color)
                pixels.set_pixel(7, display_color)
                pixels.set_pixel(22, display_color)
                pixels.set_pixel(23, display_color)
            if location == 8:
                pixels.set_pixel(54, display_color)
                pixels.set_pixel(55, display_color)
                pixels.set_pixel(70, display_color)
                pixels.set_pixel(71, display_color)
            if location == 9:
                pixels.set_pixel(102, display_color)
                pixels.set_pixel(103, display_color)
                pixels.set_pixel(118, display_color)
                pixels.set_pixel(119, display_color)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)

        pixels.show()
        time.sleep(1)        

        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        

        
    def analyze_results(winner_list):
        global X_wins
        global O_wins
        global draw_wins
        X_wins = 0
        O_wins = 0
        draw_wins = 0
        for item in winner_list:
            if item == 'X':
                X_wins = X_wins + 1
            if item == 'O':
                O_wins = O_wins + 1
            if item == 'D':
                draw_wins = draw_wins + 1
        if summary_print_bool == True:
            print("X wins: ", X_wins)
            print("O wins: ", O_wins)
            print("Draws: ", draw_wins)
            
            print("X Weight vectors: ")
            print("First move: ", weight_vectors[0])
            print(weight_vectors[0].index(max(weight_vectors[0]))+1)
            print("Second move: ", weight_vectors[1])
            print(weight_vectors[1].index(max(weight_vectors[1]))+1)
            print("Third move: ", weight_vectors[2])
            print(weight_vectors[2].index(max(weight_vectors[2]))+1)
            print("Fourth move: ", weight_vectors[3])
            print(weight_vectors[3].index(max(weight_vectors[3]))+1)
            print("Fifth move: ", weight_vectors[4])
            print(weight_vectors[4].index(max(weight_vectors[4]))+1)

            print("O Weight vectors: ")
            print("First move: ", weight_vectors_2[0])
            print(weight_vectors_2[0].index(max(weight_vectors_2[0]))+1)
            print("Second move: ", weight_vectors_2[1])
            print(weight_vectors_2[1].index(max(weight_vectors_2[1]))+1)
            print("Third move: ", weight_vectors_2[2])
            print(weight_vectors_2[2].index(max(weight_vectors_2[2]))+1)
            print("Fourth move: ", weight_vectors_2[3])
            print(weight_vectors_2[3].index(max(weight_vectors_2[3]))+1)
            print("Fifth move: ", weight_vectors_2[4])
            print(weight_vectors_2[4].index(max(weight_vectors_2[4]))+1)

    def print_board():
        print('          ',top_left, '|', top_mid, '|', top_right)
        print('          ------------')
        print('          ',mid_left, '|', mid_mid, '|', mid_right)
        print('          ------------')
        print('          ',bottom_left, '|', bottom_mid, '|', bottom_right)
        print('         ------------')
        print('\n')

    def check_for_draw():
        if len(move_memory) == 9:
            if print_bool == True:
                print("Game Over. Result: Draw")
            win_flash([1,2,3,4,5,6,7,8,9], "draw")
            raise Game_Over_Draw
            

    def check_for_win(move_history, player):
        
        if len(move_history) >= 3:
            for subset in itertools.combinations(move_history, 3):
                if 1 in subset and 5 in subset and 9 in subset:
                    if print_bool == True:
                        print("Game Over. Diagonal Win. Result: ", player, " wins")
                    win_flash([1, 5, 9], "win")
                    raise Game_Over_Winner
                if 3 in subset and 5 in subset and 7 in subset:
                    if print_bool == True:
                        print("Game Over. Diagonal Win. Result: ", player, " wins")
                    win_flash([3, 5, 7], "win")
                    raise Game_Over_Winner
                if 1 in subset and 4 in subset and 7 in subset:
                    if print_bool == True:
                        print("Game Over. Left Column Win. Result: ", player, " wins")
                    win_flash([1, 4, 7], "win")
                    raise Game_Over_Winner
                if 2 in subset and 5 in subset and 8 in subset:
                    if print_bool == True:
                        print("Game Over. Mid Column Win. Result: ", player, " wins")
                    win_flash([2, 5, 8], "win")
                    raise Game_Over_Winner
                if 3 in subset and 6 in subset and 9 in subset:
                    if print_bool == True:
                        print("Game Over. Right Column Win. Result: ", player, " wins")
                    win_flash([3, 6, 9], "win")
                    raise Game_Over_Winner
                if 1 in subset and 2 in subset and 3 in subset:
                    if print_bool == True:
                        print("Game Over. Top Row Win. Result: ", player, " wins")
                    win_flash([1, 2, 3], "win")
                    raise Game_Over_Winner
                if 4 in subset and 5 in subset and 6 in subset:
                    if print_bool == True:
                        print("Game Over. Mid Row Win. Result: ", player, " wins")
                    win_flash([4, 5, 6], "win")
                    raise Game_Over_Winner
                if 7 in subset and 8 in subset and 9 in subset:
                    if print_bool == True:
                        print("Game Over. Bottom Row Win. Result: ", player, " wins")
                    win_flash([7, 8, 9], "win")
                    raise Game_Over_Winner


    def choose_char():
        global move_char
        if move%2 == 1:
            move_char = 'X'
            
        if move%2 == 0:
            move_char = 'O'
        return move_char

    def choose_random_move():
    # Picks a random move and makes sure it hasn't been played
        global move_position
        move_position = 10
        while move_position == 10:
            test_value = random.randint(1,9)
            if test_value not in move_memory:
                move_position = test_value
                move_memory.append(move_position)
        return move_position

    def choose_weighted_move(input_move):
        # Convert the move number into an index number in the list of grid rows
        if input_move%2 == 1:
            move = int(math.floor(input_move/2) + 1)
        if input_move%2 == 0:
            move = int(input_move/2)
        global move_position
        move_position = 10
        x_move_vector = []
        o_move_vector = []

        # Choose the appropriate weight grid for X (odd) or O (even)
        if input_move%2 == 1:
            for item in weight_vectors[move-1]:
                x_move_vector.append(item)
        if input_move%2 == 0:
            for item in weight_vectors_2[move-1]:
                o_move_vector.append(item)

        while 1:
            
            if input_move%2 == 1:
                test_value = x_move_vector.index(max(x_move_vector))+1
            if input_move%2 == 0:
                test_value = o_move_vector.index(max(o_move_vector))+1
                
            #print("test value: ", test_value)
            if test_value not in move_memory:
                move_position = test_value
                move_memory.append(move_position)
                break
            else:
                if input_move%2 == 1:
                    x_move_vector[test_value-1] = -1000000000000000000000000000000000000 #prevents it from being selected by the max functino on the next iteration
                if input_move%2 == 0:
                    o_move_vector[test_value-1] = -1000000000000000000000000000000000000
                #print("move vector: ", move_vector)

    def execute_move(move_position):
    # Map the integer to a square on the board and place the x or o there
            global top_left
            global top_mid
            global top_right
            global mid_left
            global mid_mid
            global mid_right
            global bottom_left
            global bottom_mid
            global bottom_right
            
            if move_position == 1:
                top_left = move_char
            elif move_position == 2:
                top_mid = move_char
            elif move_position == 3:
                top_right = move_char
            elif move_position == 4:
                mid_left = move_char
            elif move_position == 5:
                mid_mid = move_char
            elif move_position == 6:
                mid_right = move_char
            elif move_position == 7:
                bottom_left = move_char
            elif move_position == 8:
                bottom_mid = move_char
            elif move_position == 9:
                bottom_right = move_char
            else:
                print("Something went wrong with defining the mood position")
                raise Execute_Error
            #return [top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bottom_left, bottom_mid, bottom_right]

    def print_move_result(move, move_position):
            if move%2 == 1:
                if print_bool == True:
                    print("\n Move # ", move, "...... X's move.... Move Position: ", move_position)
                x_moves.append(move_position)
            if move%2 == 0:
                if print_bool == True:
                    print("\n Move # ", move, "......O's move.... Move Position: ", move_position)
                o_moves.append(move_position)

    def print_scaffolding(game_count):
        if summary_print_bool == True:
            print("-------------------------------------------------------")
            print("             Game ", game_count+1)
            print("-------------------------------------------------------")

    def print_summary(winner_list, game_count):
        if summary_print_bool == True:
            print("----------------------------------------------------------------")
            print("             Summary ")
            print("----------------------------------------------------------------")
    ##    print("Winner's List: ", winner_list)
            print("\n Number of Games: ", game_count)
        analyze_results(winner_list)

    def choose_move(move, move_memory, x_moves, o_moves):

        global move_position


        # This first chunk looks for immediate wins and executes them
        for possible_move in range(1,10):
            temporary_moves = []
            if possible_move not in move_memory:
                if move%2 == 1: #X's move. Check if adding any move to the x_move list would result in a win condition
                    for item in x_moves:
                        temporary_moves.append(item)
                if move%2 == 0: #O's move.
                    for item in x_moves:
                        temporary_moves.append(item)
                temporary_moves.append(possible_move)
                for subset in itertools.combinations(temporary_moves,3):
                    if (1 in subset and 5 in subset and 9 in subset) or (3 in subset and 5 in subset and 7 in subset) or (1 in subset and 4 in subset and 7 in subset) or (2 in subset and 5 in subset and 8 in subset) or (3 in subset and 6 in subset and 9 in subset) or (1 in subset and 2 in subset and 3 in subset) or (4 in subset and 5 in subset and 6 in subset) or (7 in subset and 8 in subset and 9 in subset):
                        move_position = possible_move
                        move_memory.append(move_position)
                        return

        # This second chunk looks for immediate threats and blocks them
        for possible_move in range(1,10):
            temporary_moves = []
            if possible_move not in move_memory:
                if move%2 == 1: #X's move. Check if adding any move to o_move list would result in a win condition
                    for item in o_moves:
                        temporary_moves.append(item)
                if move%2 == 0: #O's move.
                    for item in x_moves:
                        temporary_moves.append(item)
                temporary_moves.append(possible_move)
                for subset in itertools.combinations(temporary_moves,3):
                    if (1 in subset and 5 in subset and 9 in subset) or (3 in subset and 5 in subset and 7 in subset) or (1 in subset and 4 in subset and 7 in subset) or (2 in subset and 5 in subset and 8 in subset) or (3 in subset and 6 in subset and 9 in subset) or (1 in subset and 2 in subset and 3 in subset) or (4 in subset and 5 in subset and 6 in subset) or (7 in subset and 8 in subset and 9 in subset):
                        #print("Win imminent for opponent!")
                        move_position = possible_move
                        #print("Move position to avoid imminent win is: ", move_position)
                        move_memory.append(move_position)
                        return
                    
        
        if move%2 == 0 and game_count > math.floor(number_of_games/1) and x_play_with_weights_bool == False and o_play_with_weights_bool == False: #This line can be used to force x to start playing with weights partway through the training
            x_play_with_weights = not x_play_with_weights_bool
            o_play_with_weights = o_play_with_weights_bool
        else:
            x_play_with_weights = x_play_with_weights_bool
            o_play_with_weights = o_play_with_weights_bool
            
        if x_play_with_weights == True and o_play_with_weights == False:
            if move%2 == 1:
                choose_weighted_move(move)
            if move%2 == 0:
                choose_random_move()
        elif x_play_with_weights == True and o_play_with_weights == True:
            choose_weighted_move(move)
        else:
            choose_random_move()


    # Outer while loop iterates through number of games. It runs the game then prints the end-state board and increments the game count.
    # Inner while loop plays the game. It checks for a win then chooses the appropriate character, chooses a random move, and executes the move by setting the character into a variable. It then increments the move count.
    while game_count < number_of_games:

        if display_on_lights_boolean == 1:
            pixels.clear()
            pixels.show()
        move_memory = []
        x_moves = []
        o_moves = []
        move = 1

        top_left = '-'
        top_mid = '-'
        top_right = '-'
        mid_left = '-'
        mid_mid = '-'
        mid_right = '-'
        bottom_left = '-'
        bottom_mid = '-'
        bottom_right = '-'

        if print_bool == True:
            print_scaffolding(game_count)
        
        while 1:

            try: #Check for end of game. If game over, subfunction will raise Game_Over exception, causing except below which will break
                check_for_win(x_moves, "X")
                check_for_win(o_moves, "O")
                check_for_draw()
                choose_char()
                choose_move(move, move_memory, x_moves, o_moves)
                execute_move(move_position)
                if display_on_lights_boolean == 1:
                    display_on_lights(x_moves, 'X')
                    display_on_lights(o_moves, 'O')
                print_move_result(move, move_position)
                if print_every_move_bool == True:
                    print_board()
            except Game_Over_Winner:
                winner_list.append(move_char)
                update_weight_vectors(x_moves, move_char)
                break
            except Game_Over_Draw:
                winner_list.append("D")
                break
            except Execute_Error:
                break

            move = move+1

        if print_bool == True:
            print_board()
      
        game_count = game_count + 1

    print_summary(winner_list, game_count)
    x_weight_vector_store = open('store.pck1', 'wb')
    o_weight_vector_store = open('store.pck2','wb')
    pickle.dump(weight_vectors, x_weight_vector_store)
    pickle.dump(weight_vectors_2, o_weight_vector_store)
    x_weight_vector_store.close()
    o_weight_vector_store.close()
    

    if display_on_lights_boolean == 1:
        GPIO.cleanup()
    return [X_wins, O_wins, draw_wins]
