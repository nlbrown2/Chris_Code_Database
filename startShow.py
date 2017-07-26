def startShow(showName):

    #showName = "Tic_tac_toe"

    from start_hue_show import start_hue_show
    from start_autonomous_snake import start_autonomous_snake
    from start_reversi import start_reversi
    from start_tic_tac_toe import start_tic_tac_toe
    from start_clock import start_clock

    if showName == "Hue Show":
        #def start_hue_show(wait1=0, speed1=1.75, wait2=0, speed2=1.75, wait3=0, speed3=1.75, wait4=0, speed4=1.75)
        #requires non_serialized_hue_shift, random_light_display, serialized_hue_shift, and simultaneous_hue_shift
        start_hue_show()

    if showName == "Snake":
        #def autonomous_snake(sleep_time=0.5, wait_times=[0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.15, 0.2, 0.2], number_of_nom_noms=2, number_of_bombs=5, number_of_caffeine_pills=5, level_0_nom_nom=10, level_1_nom_nom=7, level_2_nom_nom=4, display_on_lights_boolean=1)
        #sleep_time is the time between each step, wait_times correspond to the sleep_times when the snake has a caffeine pill (he slows down over the duration of the pill)
        #the level_#_nom_nom variables specify the weight values given to certain moves. e.g. if a nom_nom is right next to you (level 0), it gets a lot of value, but if it's far away (level 2), it matters less so it gets less value
        start_autonomous_snake(display_on_lights_boolean=0)
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call

    if showName == "Reversi":
        #def start_reversi(train='no', iterations=1000,print_bool_no=1, black_input_no='starter_input', white_input_no='starter_input', print_bool_yes=0, black_input_yes='computer_weight_capture', white_input_yes='computer_random', reset_weight_grid_boolean=0, display_on_lights_boolean=1)
        #train determines whether the computer trains. If no, plays 1 game. If yes, plays number of games specified in iterations
        #print_bool_no and print_bool_yes can either be 1 or 0 to decide if there is text output in the conditions that train = 'no' or 'yes'
        #black_input_no, black_input_yes, white_input_no, and white_input_yes are set to determine the strategies that each color will play
        #Options for black_input and white_input:
            #starter_input -> asks user for strategy (computer_weight_capture, computer_random, or human)
            #computer_weight_capture -> uses weight_capture_strategy_edge_priority 20% of the time, and random strategy 80% of the time
            #computer_random -> picks a random strategy
            #human -> the user gets to play
        #The possible strategies are:
            #first_max_score -> chooses the move that will capture the most pieces, and if there are multiple moves that are equal in this regard, it will pick the first one it finds
            #weight_grid_strategy -> chooses the move that will capture the most grid points. If there's a tie, chooses the first one it finds
            #weight_grid_strategy_edge_priority -> chooses the move that will capture the most grid points. If there is a tie, chooses the one closest to the edge.        
            #max_score_priority_closest_to_cent -> chooses the move that will capture the most pieces and, if multiple moves are equal in this regard, is closest to the center 
            #max_score_priority_closest_to_edge -> chooses the move that will capture the most pieces and, if multiple moves are equal in thsi regard,  is closest to the edge
        #Code flow: start_reversi calls play_a_game which calls strategy_picker to get a strategy then calls Black_Move and White_Move to actually make the moves. These functions call move_executor to update the board then do some score-keeping duties. Move_executor calls calculate_legal_moves to get a list of legal moves that it feeds into strategy_executor to figure out where to place the piece. It places the piece then returns to White_Move or Black_Move which does admin duties then returns to play_a_game which does more admi duties, then returns to start_reversi which does some admin duties then calls the next game.
        #Requires Black_and_white_moves, board_setup, calculate_legal_moves, move_executor, play_a_game, reset_weight_grid, strategy_executor, strategy_picker, display_reversi_board_on_lights, and update_weight_grid
        start_reversi(reset_weight_grid_boolean=0, train='yes', iterations=100, display_on_lights_boolean=0)
        #IMPORTANT: The first time you run the Reversi program, the reset_weight_grid_boolean has to equal 1. This will actually create the weight grid. However, if it stays 1 on subsequent calls, the computer will have to restart its training every time and cannot learn from past sessions
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call

    if showName == "Tic_tac_toe":
        #def start_tic_tac_toe(display_on_lights_boolean=1, summary_print_bool=True, input_number_of_trains=1000, input_number_of_games=1, x_win_weighting=1, o_win_weighting=1)\
        #summary_print_bool determines if a summary of the game session will be printed to the screen after all of the games have been played
        #input_number_of_trains is the nmber of times that the computer will train against itself before actually beginning to use the training
        #input_number_of_games is the number of games that the computer will play after it has trained
        #Requires tic_tac_toe_1
        start_tic_tac_toe(display_on_lights_boolean=0, input_number_of_trains=100000, input_number_of_games=5, summary_print_bool=False)
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call
    if showName == "Clock":
        #This program will call either digital_clock_vertical or digital_clock_horizontal depending on whether orientation = 'vertical' or 'horizontal'
        #The vertical clock is very basic and only takes one argument: display_on_lights_bool
        #The horizontal clock is more complicated. It has a timer feature that is set using the timer_value and the timer_unit. The display_on_lights_bool is also accepted as an input.
        start_clock(orientation='horizontal', display_on_lights_bool=0, timer_value=1, timer_unit="minutes")
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_bool to 1
        

        
