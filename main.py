from blessed import Terminal
import numpy as np
import time

term = Terminal()
grid = [[np.random.randint(0,2) for j in range(20)] for i in range(15)]
grid = np.array(grid)

def check_neighbors(row, col):
    global grid
    total = 0
    for i,j in ([0,1],[-1,0],[0,-1],[1,0], [1,1], [1,-1], [-1,1], [-1,-1]):
            if (row+i >= 0 and row+i < grid.shape[0] and 
                col+j >= 0 and col+j < grid.shape[1]):
                if(grid[row+i,col+j] == 1):
                    total += 1
    return total

def apply_conway():
    global grid
    tmp = grid.copy()
    for i,j in np.ndindex(grid.shape):
        n = check_neighbors(i,j)
        if(tmp[i,j] == 1 and (n == 2 or n == 3)):
            tmp[i,j] = 1
        elif(tmp[i,j] == 0 and n == 3):
            tmp[i,j] = 1
        else:
            tmp[i,j] = 0
    grid = tmp


while True:
    print(term.home + term.clear)
    for row in grid:
        for item in row:
            if(item == 1):
                print(term.red("■ ")+term.white(""),end="")
            else:
                print("■ ",end="")
        print("")
    time.sleep(0.3)
    apply_conway()