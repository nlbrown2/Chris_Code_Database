def update_weight_grid(board, winner, print_bool):
    #print("in update weight grid")

    import numpy as np
    
    if winner == 'black':
        weight_grid = np.load('weight_grid.npy')
        if print_bool == 1:
            print('Weight Grid: ')
            print(weight_grid)
        for i in range(8):
            for j in range(8):
                if board[i,j] == 2:
                    weight_grid[i,j] += 1
                if board[i,j] == 1:
                    weight_grid[i,j] -= 1
        if print_bool == 1:
            print('Updated Weight Grid: ')
            print(weight_grid)
        np.save('weight_grid', weight_grid)
        #print("Saved!")
