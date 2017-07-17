def strategy_picker(move, black_input, white_input):

    ## Determines which strategy each player should use. At the moment, black uses the weight capture strategy 20% of the time and random the other 80% of the time. White is always random. White can be set to human player
    
    import random

    possible_strategies = ['first_max_score', 'max_score_priority_closest_to_cent', 'max_score_priority_closest_to_edge']

    while black_input == 'starter_input':
        
        black_input = input('What is black\'s strategy? [computer_weight_capture, computer_random, human] >> ')
        
        if black_input not in ['computer_weight_capture', 'computer_random', 'human']:
            print('not a possible strategy. try again')
            black_input = 'starter_input'

    while white_input == 'starter_input':
        
        white_input = input('What is white\'s strategy? [computer_weight_capture, computer_random, human] >> ')
        
        if white_input not in ['computer_weight_capture', 'computer_random', 'human']:
            print('not a possible strategy. try again')
            white_input = 'starter_input'
    
    if black_input == 'computer_weight_capture':

        x = random.random()
        if x < 0.2:
            black_strategy = 'weight_capture_strategy_edge_priority'
        if x >= 0.2:
            black_strategy = possible_strategies[random.randint(0,2)]

    if black_input == 'computer_random':
        black_strategy = possible_strategies[random.randint(0,2)]

    if black_input == 'human':
        black_strategy = 'human_player'
            

    if white_input == 'computer_weight_capture':

        x = random.random()
        if x < 0.2:
            white_strategy = 'weight_capture_strategy_edge_priority'
        if x >= 0.2:
            white_strategy = possible_strategies[random.randint(0,2)]

    if white_input == 'computer_random':
        white_strategy = possible_strategies[random.randint(0,2)]

    if white_input == 'human':
        white_strategy = 'human_player'


    return [black_strategy, white_strategy, black_input, white_input]

    ##        if move >= 30 and move < 50:
    ##            if x < 0.7:
    ##                black_strategy = 'weight_capture_strategy_edge_priority'
    ##            if x >= 0.7:
    ##                black_strategy = possible_strategies[random.randint(0,2)]
    ##
    ##        if move >= 50:
                #black_strategy = 'weight_capture_strategy_edge_priority'
            #black_strategy = possible_strategies[random.randint(0,2)]
