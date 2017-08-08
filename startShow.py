def startShow(show_dict):
    #show_dict = {'name': 'Big_Text_Scroller'} #used for testing
    ## Accepts a dictionary that includes a show name and the approriate arguments. It then unpacks the arguments and calls the appropriate functions.

    try:
        showName = show_dict['name']
    except:
        print("Couldn't get the show name from the dict!")
        #return
        

    #showName = "Clock"

    from start_hue_show import start_hue_show
    from start_autonomous_snake import start_autonomous_snake
    from start_reversi import start_reversi
    from start_tic_tac_toe import start_tic_tac_toe
    from start_clock import start_clock
    from start_text_scroller import start_text_scroller
    from start_big_text_scroller import start_big_text_scroller

    if showName == "Hue Show":
        #def start_hue_show(wait1=0, speed1=1.75, wait2=0, speed2=1.75, wait3=0, speed3=1.75, wait4=0, speed4=1.75)
        #requires non_serialized_hue_shift, random_light_display, serialized_hue_shift, and simultaneous_hue_shift

        ### Defaults ###
        wait1 = 0
        speed1 = 1.75
        wait2 = 0
        speed2 = 1.75
        wait3 = 0
        speed3 = 1.75
        wait4 = 0
        speed4 = 1.75

        ### Replace defaults with arguments from queue ###
        try: wait1 = show_dict['wait1']
        except: print("Warning: could not get wait1")
        try: speed1 = show_dict['speed1']
        except: print("Warning: could not get speed1")
        try: wait2 = show_dict['wait2']
        except: print("Warning: could not get wait2")
        try: speed2 = show_dict['speed2']
        except: print("Warning: could not get speed2")
        try: wait3 = show_dict['wait3']
        except: print("Warning: could not get wait3")
        try: speed3 = show_dict['speed3']
        except: print("Warning: could not get speed3")
        try: wait4 = show_dict['wait4']
        except: print("Warning: could not get wait4")
        try: speed4 = show_dict['speed4']
        except: print("Warning: could not get speed4")

        ### Call program ###

        start_hue_show(wait1, speed1, wait2, speed2, wait3, speed3, wait4, speed4)

    if showName == "Snake":
        #def autonomous_snake(sleep_time=0.5, wait_times=[0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.15, 0.2, 0.2], number_of_nom_noms=2, number_of_bombs=5, number_of_caffeine_pills=5, level_0_nom_nom=10, level_1_nom_nom=7, level_2_nom_nom=4, display_on_lights_boolean=1)
        #sleep_time is the time between each step, wait_times correspond to the sleep_times when the snake has a caffeine pill (he slows down over the duration of the pill)
        #the level_#_nom_nom variables specify the weight values given to certain moves. e.g. if a nom_nom is right next to you (level 0), it gets a lot of value, but if it's far away (level 2), it matters less so it gets less value
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call
        
        ### Defaults ###
        sleep_time = 0.5
        wait_times = [0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.15, 0.2, 0.2]
        number_of_nom_noms = 2
        nmber_of_bombs = 5
        number_of_caffeine_pills = 5
        level_0_nom_nom = 10
        level_1_nom_nom = 7
        level_2_nom_nom = 4
        display_on_lights_boolean = False

        ### Replace defaults with arguments from queue ###
        try: sleep_time = show_dict['sleep_time']
        except: print("Warning: could not get sleep_time")
        try: wait_times = show_dict['wait_times']
        except: print("Warning: could not get wait_times")
        try: number_of_nom_noms = show_dict['number_of_nom_noms']
        except: print("Warning: could not get number_of_nom_noms")
        try: number_of_bombs = show_dict['number_of_bombs']
        except: print("Warning: could not get number_of_bombs")
        try: number_of_caffeine_pills = show_dict['number_of_caffeine_pills']
        except: print("Warning: could not get number_of_caffeine_pills")
        try: level_0_nom_nom = show_dict['level_0_nom_nom']
        except: print("Warning: could not get level_0_nom_nom")
        try: level_1_nom_nom = show_dict['level_1_nom_nom']
        except: print("Warning: could not get level_1_nom_nom")
        try: level_2_nom_nom = show_dict['level_2_nom_nom']
        except: print("Warning: could not get level_2_nom_nom")
        try: display_on_lights_boolean = show_dict['display_on_lights_boolean']
        except: print("Warning: could not get display_on_lights_boolean")

        ### Call program ###
        
        start_autonomous_snake(sleep_time, wait_times, number_of_nom_noms, nomber_of_bombs, number_of_caffeine_pills, level_0_nom_nom, level_1_nom_nom, level_2_nom_nom, display_on_lights_boolean)
        

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
        #IMPORTANT: The first time you run the Reversi program, the reset_weight_grid_boolean has to equal 1. This will actually create the weight grid. However, if it stays 1 on subsequent calls, the computer will have to restart its training every time and cannot learn from past sessions
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call


        ### Defaults ###
        train = 'no'
        iterations = 1000
        print_bool_no = 1
        black_input_no = 'starter_input'
        white_input_no = 'starter_input'
        print_bool_yes = 0
        black_input_yes = 'computer_weight_capture'
        white_input_yes = 'computer_random'
        reset_weight_grid_boolean = 0
        display_on_lights_boolean = 1

        ### Replace defaults with arguments from queue ###
        try: train = show_dict['train']
        except: print("Warning: could not get train")
        try: iterations = show_dict['iterations']
        except: print("Warning: could not get iterations")
        try: print_bool_no = show_dict['print_bool_no']
        except: print("Warning: could not get print_bool_no")
        try: black_input_no = show_dict['black_input_no']
        except: print("Warning: could not get black_input_no")
        try: white_input_no = show_dict['white_input_no']
        except: print("Warning: could not get white_input_no")
        try: print_bool_yes = show_dict['print_bool_yes']
        except: print("Warning: could not get print_bool_yes")
        try: black_input_yes = show_dict['black_input_yes']
        except: print("Warning: could not get black_input_yes")
        try: white_input_yes = show_dict['white_input_yes']
        except: print("Warning: could not get white_input_yes")
        try: reset_weight_grid_boolean = show_dict['reset_weight_grid_boolean']
        except: print("Warning: could not get reset_weight_grid_boolean")
        try: display_on_lights_boolean = show_dict['display_on_lights_boolean']
        except: print("Warning: could not get display_on_lights_boolean")

        ### Call program ###

        start_reversi(train, iterations, print_bool_no, black_input_no, white_input_no, print_bool_yes, black_input_yes, white_input_yes, reset_weight_grid_boolean, display_on_lights_boolean)

    if showName == "Tic_tac_toe":
        #def start_tic_tac_toe(display_on_lights_boolean=1, summary_print_bool=True, input_number_of_trains=1000, input_number_of_games=1, x_win_weighting=1, o_win_weighting=1)
        #summary_print_bool determines if a summary of the game session will be printed to the screen after all of the games have been played
        #input_number_of_trains is the nmber of times that the computer will train against itself before actually beginning to use the training
        #input_number_of_games is the number of games that the computer will play after it has trained
        #Requires tic_tac_toe_1
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_boolean to 1 or omit from function call

        ### Defaults ###
        display_on_lights_boolean = 1
        summary_print_bool = True
        input_number_of_trains = 10000
        input_number_of_games = 1
        x_win_weighting = 1
        o_win_weighting = 1

        ### Replace defaults with arguments from queue ###
        try: display_on_lights_boolean = show_dict['display_on_lights_boolean']
        except: print("Warning: could not get display_on_lights_boolean")
        try: summary_print_bool = show_dict['summary_print_bool']
        except: print("Warning: could not get summary_print_bool")
        try: input_number_of_trains = show_dict['input_number_of_trains']
        except: print("Warning: could not get input_number_of_trains")
        try: input_number_of_games = show_dict['input_number_of_games']
        except: print("Warning: could not get input_number_of_games")
        try: x_win_weighting = show_dict['x_win_weighting']
        except: print("Warning: could not get x_win_weighting")
        try: o_win_weighting = show_dict['o_win_weighting']
        except: print("Warning: could not get o_win_weighting")

        ### Call program ###
        
        start_tic_tac_toe(display_on_lights_boolean, summary_print_bool, input_number_of_trains, input_number_of_games, x_win_weighting, o_win_weighting)


    if showName == "Clock":
        #def start_clock(orientation = 'horizontal', display_on_lights_bool=0, timer_value=1, timer_unit="minutes")
        #This program will call either digital_clock_vertical or digital_clock_horizontal depending on whether orientation = 'vertical' or 'horizontal'
        #The vertical clock is very basic and only takes one argument: display_on_lights_bool
        #The horizontal clock is more complicated. It has a timer feature that is set using the timer_value and the timer_unit. The display_on_lights_bool is also accepted as an input.
        #IMPORTANT: If you want to see it on the lights, change the display_on_lights_bool to 1

        ### Defaults ###
        orientation = 'horizontal'
        display_on_lights_bool = 0
        timer_value = 1
        timer_unit = "minutes"

        ### Replace defaults with arguments from queue ###
        try: orientation = show_dict['orientation']
        except: print("Warning: could not get orientation")
        try: display_on_lights_bool = show_dict['display_on_lights_bool']
        except: print("Warning: could not get display_on_lights_bool")
        try: timer_value = show_dict['timer_value']
        except: print("Warning: could not get timer_value")
        try: timer_unit = show_dict['timer_unit']
        except: print("Warning: could not get timer_unit")

        ### Call program ###
        start_clock(orientation, display_on_lights_bool, timer_value, timer_unit)
        
    if showName == "Text_Scroller":
        #def start_text_scroller(input_string_top = "Go Blue!", input_string_bottom = "Go Blue!", rainbow_bool = False, lights_bool = False, text_color_top = "Blue", text_color_bottom = "Yellow")
        # Scrolls two strings across the board; one on top and one on bottom. Rainbow_bool will print each letter in a different color. Otherwise, specify the text_color_top and text_color_bottom to print the entire string in one color.
        #Also takes continuous_bool to determine if it should loop the message forever
        # IMPORTANT: Set lights_bool to actually see this on the lights
        # IMPORTANT: The text colors can only be blue, red, yellow, green, or purple as of this writing.
        # IMPORTANT: Probably lots of bugs in this program

        ### Defaults ###
        input_string_top = "Go Blue!"
        input_string_bottom = "Go Blue!"
        rainbow_bool = False
        lights_bool = False
        text_color_top = "Blue"
        text_color_bottom = "Yellow"
        loop_count = -1

        ### Replace defaults with arguments from queue ###
        try: input_string_top = show_dict['input_string_top']
        except: print("Warning: could not get input_string_top")
        try: input_string_bottom = show_dict['input_string_bottom']
        except: print("Warning: could not get input_string_bottom")
        try: rainbow_bool = show_dict['rainbow_bool']
        except: print("Warning: could not get rainbow_bool")
        try: lights_bool = show_dict['lights_bool']
        except: print("Warning: could not get lights_bool")
        try: text_color_top = show_dict['text_color_top']
        except: print("Warning: could not get text_color_top")
        try: text_color_bottom = show_dict['text_color_bottom']
        except: print("Warning: could not get text_color_bottom")
        try: loop_count = show_dict['loop_count']
        except: print("Warning: could not get loop_count")


        ### Call program ###
        if loop_count == -1:
            while 1:
                start_text_scroller(input_string_top, input_string_bottom, rainbow_bool, lights_bool, text_color_top, text_color_bottom)
        elif loop_count > 0:
            for i in range(loop_count):
                start_text_scroller(input_string_top, input_string_bottom, rainbow_bool, lights_bool, text_color_top, text_color_bottom)
        else:
            print("Invalid entry for loop_count")

    if showName == "Big_Text_Scroller":

        ## Same as Text_Scroller but uses whole grid so characters are bigger
        # Also takes continuous_bool to determine if it should loop the message forever
        
        ### Defaults ###
        input_string = "Go Blue!"
        rainbow_bool = False
        lights_bool = False
        text_color = "Yellow"
        loop_count = 2

        ### Replace defaults with arguments from queue ###
        try: input_string = show_dict['input_string']
        except: print("Warning: could not get input_string")
        try: rainbow_bool = show_dict['rainbow_bool']
        except: print("Warning: could not get rainbow_bool")
        try: lights_bool = show_dict['lights_bool']
        except: print("Warning: could not get lights_bool")
        try: text_color = show_dict['text_color']
        except: print("Warning: could not get text_color")
        try: loop_count = show_dict['loop_count']
        except: print("Warning: could not get loop_count")


        ### Call program ###
        if loop_count == -1:
            while 1:
                start_big_text_scroller(input_string, rainbow_bool, lights_bool, text_color)
        elif loop_count > 0:
            for i in range(loop_count):
                start_big_text_scroller(input_string, rainbow_bool, lights_bool, text_color)
        else:
            print("Invalid entry for loop_count")
        
