##When writing this READ_ME, I had trouble remembering exactly where certain operations in my code occurred simply because I have so many functions. I wanted to make lots of functions so that I could change the operation
##very easily, but I fear that I've made everything way too complicated, especially with all of the passing of variables that I have to do. In any case, good luck understanding this. Feel free to ask me questions.
##
##The function you'll want to start at is executive_control. At the top, you'll need to change the path to wherever you are putting
##all of these files. I think there's another function where you have to change the path as well. At the top you can choose if you want to reset the weight grid (comment out or not) and if you want to train
##the computer to update the weight grid. To start, the reset is commented out and train is set to no. As such, only one game will be played.
##Print_bool is a variable that chooses if the program displays output. This is set to 1 (yes) in the if train == 'no' block.
##First, the program calls board_setup which uses numpy (you'll need to install this) to setup the board with the first four moves.
##Then, the line winner = play_a_game(...) actually calls the function that will execute the game. It sends the board, the print_bool, and two
##dummy variables.
##
##play_a_game calls black and white moves and does some handling of the end state of the game. It contains a for loop that iterates through moves until
##the end of the game is reached. Immediately, strategy_picker is called, which chooses the strategy that will be used by each player.
##
##strategy_picker asks the user what they want the high level strategy for each player to be. The first option is 'computer_weight_capture'. This strategy uses the weight grid
##that we talked about. It looks at how much value (not pieces, but actualy grid value) each move would capture and then the chooses the move with the highest value.
##Essentially, it chooses to capture squares that have been most occupied at the end of past winning games.  However, I don't want this strategy to run all of the time
##because I fear it would over-train the weight grid. So, I only use the strategy 20% of the time. The other 20% of the time, and random lower level strategy is chosen.
##The second high level strategy is 'computer_random' which always chooses a random lower-level strategy. The final option is 'human' which allows the user to play as one or both of the players.
##Let's talk about the lower-level strategies. At the moment there are three. They are all basically the same. They each look at every legal move and count how many pieces would be
##flipped over by executing that move. All strategies looks for the moves that optimize this value. The difference is in how the stratgies handle ties between legal moves.
##'first_max_score' uses the first location that it analyzed that produced a maximum of all possible locations. 'max_score_priority_closest_to_cent' chooses the one that is closest to the
##center of the board. 'max_score_priority_closest_to_edge' chooses the move that is closest to the edge.
##
##Going back to play_a_game, ignore anything that has [-100]. That is my condition to check for an end-of-game state. If the game is over, that [-100] is passed around the functions all the way up to play_a_game.
##When attempts to execute both black and white moves returns [-100], a winner is chosen. This is all handled at the bottom of play_a_game/
##Most of time (when the game is not over), Black_Move or White_Move are called, depending on whose turn it is. These functions analyze and make moves and return the current score after the move, which play_a_game displays.
##
##Let's talk about Black_Move and White_Move. They're basically identical so we'll just look at Black_Move. All this function does is call another function, move_executor, and print the new board after a move is excecuted.
##Then it figures out what the new score is and returns it to play_a_game
##
##move_executor first calls calculate_legal_moves which finds all the possible moves and the corresponding scores (number of pieces flipped) associated with each move. In calculate_legal_moves, I make vectors like legal_moves_right and scores_right to
##categorize the move by which direction it is active in (right indicates that pieces to the right will be flipped). Since a move can flip pieces in multiple directions, it can exist in multiple matrices. This is all very dirty code. Even dirtier is at the end
##of calculate_legal_moves where I add all of the directional scores of each legal move to make a master list of legal_moves with a master list of scores that takes into account flips in every direction. In any case, calculate_legal_moves returns a bunch of these
##vectors including a vector called legal_move_index that contains each of the directional legal move vectors, and a vector called score_index which does the same thing for scores. These vectors are used in move_executor later. After all of the legal moves have
##been found, they are passed into strategy_executor which actually implements the strategies that were discussed in strategy_picker and returns a single move, stored in location_to_place. This is the chosen move. move_executor then does the work of actually flipping pieces.
##It consults the legal_move_index to find which directions it needs to flip pieces, then uses the score_index to figure out how many pieces to flip in each direction, then actually executes the flips. It returns the updated board to the Black_Move and White_Move
##functions which count the number of white and black squares to get a score.
##
##So, from the ground up, calculate_legal_moves makes a bunch of lists of legal_moves and the corresponding flipped-piece scores (along with the weight_grid capture scores), then sends the info to the strategy_executor which chooses a specific move.
##The move_executor actually does the flipping of pieces and returns the updated board to the Black_Move and White_Move functions which figure out the new score and print the board to the screen. The Move functions are called by play_a_game
##which simply iterates through lots of moves, choosing a new strategy for each player on every move and calling the appropriate function depending on whose move it is. The executive_control function is there to control whether the program is training or not.
##
##Let's talk about the weight grid a little bit. The grid is handled by numpy and is loaded and saved every time it is used. When legal moves are calcualted and the score corresponding to each move is found, a capture score is also generated in the same way - every piece
##that would be flipped has a corresponding value on the weight_grid, and these values are summed. The capture scores are used in the capture score strategy which chooses the move with the highest capture score. When the game is over, and the end-game code runs
##at the end of play_a_game, if black won, every square in weight_grid whose corresponding square on the board has a black piece gets a +1 increment, and every white piece gets a -1 decrement. When training the computer, whenever this board is displayed it is normalized.                                                        
##                                                       
