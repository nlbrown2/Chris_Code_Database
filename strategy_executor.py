def strategy_executor(strategy, net_legal_moves, net_scores, print_bool, net_capture_scores, human_player_move):

    import math
    import numpy as np
    net_center_distances = []
    net_center_locations = []
    net_edge_distances = []
    net_edge_locations = []
    legal_move_grid_values = []
    candidate_locations = []
    candidate_scores = []


    #Human player
    if strategy == 'human_player':
        print(human_player_move)
        location_to_place = [human_player_move[0], human_player_move[1]]

    #Pick first max score strat
    if strategy == 'first_max_score':
        location_to_place = net_legal_moves[net_scores.index(max(net_scores))]

    #Max score priority center strategy which chooses the move that will capture the most pieces and is closest to the center
    if strategy == 'max_score_priority_closest_to_cent':
        for item in net_legal_moves:
            if net_scores[net_legal_moves.index(item)] == max(net_scores):
                dist_from_cent = math.sqrt(pow((item[0]-3),2)+pow((item[1]-3),2))
                net_center_locations.append(item)
                net_center_distances.append(dist_from_cent)
        location_to_place = net_center_locations[net_center_distances.index(min(net_center_distances))]
        if location_to_place != strategy_executor('first_max_score', net_legal_moves, net_scores, print_bool, net_capture_scores, human_player_move):
            if print_bool == 1:
                print('Using the max score with priority on center strategy to make a different choice than first max score strategy')

    #Max score priority edges strategy which chooses the move that will capture the most pieces and is closest to the edges
    if strategy == 'max_score_priority_closest_to_edge':
        for item in net_legal_moves:
            if net_scores[net_legal_moves.index(item)] == max(net_scores):
                if item[0] > 3 and item[1] > 3:  #Four of these conditions to figure out which edge to check
                    dist_from_edge = math.sqrt(pow((item[0]-7),2)+pow((item[1]-7),2))
                if item[0] > 3 and item[1] <= 3:
                    dist_from_edge = math.sqrt(pow((item[0]-7),2)+pow((item[1]-0),2))
                if item[0] <= 3 and item[1] > 3:
                    dist_from_edge = math.sqrt(pow((item[0]-0),2)+pow((item[1]-7),2))
                if item[0] <= 3 and item[1] <= 3:
                    dist_from_edge = math.sqrt(pow((item[0]-0),2)+pow((item[1]-0),2))
                net_edge_locations.append(item)
                net_edge_distances.append(dist_from_edge)
        location_to_place = net_edge_locations[net_edge_distances.index(min(net_edge_distances))]
        if location_to_place != strategy_executor('first_max_score', net_legal_moves, net_scores, print_bool, net_capture_scores, human_player_move):
                if print_bool == 1:
                    print('Using the max score with priority on edges strategy to make a different choice than first max score strategy')

    # Weight grid strategy which only looks at the value of the location selected
    if strategy == 'weight_grid_strategy':
        weight_grid = np.load('weight_grid.npy')
        for item in net_legal_moves:
            legal_move_grid_values.append(weight_grid[item[0], item[1]])
        if print_bool == 1:
            print ('Legal Move Grid Values: ', legal_move_grid_values)
        for item in net_legal_moves:
            if legal_move_grid_values[net_legal_moves.index(item)] == max(legal_move_grid_values): #for every legal move, if the corresponding weight_grid value is the greatest of all legal moves
                candidate_locations.append(item)
                candidate_scores.append(net_scores[net_legal_moves.index(item)])
        if print_bool == 1:
            print('Candidate locations: ', candidate_locations)
            print('Candidate_scores: ', candidate_scores)
        location_to_place = strategy_executor('max_score_priority_closest_to_edge', candidate_locations, candidate_scores, print_bool, net_capture_scores, human_player_move)

    # Weight capture strategy which chooses the move that will capture the most grid points and is closest to the edge
    if strategy == 'weight_capture_strategy_edge_priority':
        if print_bool == 1:
            print('Camdidate locations: ', net_legal_moves)
            print('Candidate capture scores: ', net_capture_scores)
        for item in net_legal_moves:
            if net_capture_scores[net_legal_moves.index(item)] == max(net_capture_scores): #for every legal move, if the corresponding capture score is the greatest of all legal moves
                if item[0] > 3 and item[1] > 3:  #Four of these conditions to figure out which edge to check
                    dist_from_edge = math.sqrt(pow((item[0]-7),2)+pow((item[1]-7),2))
                if item[0] > 3 and item[1] <= 3:
                    dist_from_edge = math.sqrt(pow((item[0]-7),2)+pow((item[1]-0),2))
                if item[0] <= 3 and item[1] > 3:
                    dist_from_edge = math.sqrt(pow((item[0]-0),2)+pow((item[1]-7),2))
                if item[0] <= 3 and item[1] <= 3:
                    dist_from_edge = math.sqrt(pow((item[0]-0),2)+pow((item[1]-0),2))
                net_edge_locations.append(item)
                net_edge_distances.append(dist_from_edge)
        location_to_place = net_edge_locations[net_edge_distances.index(min(net_edge_distances))]
        if location_to_place != strategy_executor('first_max_score', net_legal_moves, net_scores, print_bool, net_capture_scores, human_player_move):
                if print_bool == 1:
                    print('Using the weight grid capture with priority on edges strategy to make a different choice than first max score strategy')


    return location_to_place
