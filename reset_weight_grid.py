def reset_weight_grid():
    import numpy as np
    import os
    #path = "C:\\Users\\myran\\Desktop" #change for pi
    #os.chdir(path)

    #weight_grid = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]])
    weight_grid = np.zeros([8,8])
    np.save('weight_grid', weight_grid)
    weight_grid = np.load('weight_grid.npy')
