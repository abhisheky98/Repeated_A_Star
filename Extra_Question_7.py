from Grid_Generator import gen_grid
import timeit
import pandas as pd

def find_path(parent, dim, si, sj):
    i,j = dim-1, dim-1
    path = [(dim-1, dim-1)]
    while (i, j) != (si, sj):
        path.insert(0, parent[i][j])
        (i, j) = parent[i][j]
    return(path)

def BFS(dim, grid, si, sj):
    
    result = False
    
    fringe = [(si, sj)]
    cells = 0
    
    p = [[-1 for i in range(dim)] for j in range(dim)]
    p[si][sj] = 0
    
    while len(fringe) != 0:
        (i, j) = fringe.pop(0)
        cells = cells + 1
        #print("a")
        if (i, j) == (dim-1, dim-1):
            result = True
            break
        if i-1 >= 0 and grid[i-1][j] != 1 and p[i-1][j] == -1:
            p[i-1][j] = (i, j)
            fringe.append((i-1,j))
        if j+1 < dim and grid[i][j+1] != 1 and p[i][j+1] == -1:
            p[i][j+1] = (i, j)
            fringe.append((i,j+1))
        if i+1 < dim and grid[i+1][j] != 1 and p[i+1][j] == -1:
            p[i+1][j] = (i, j)
            fringe.append((i+1,j))
        if j-1 >= 0 and grid[i][j-1] != 1 and p[i][j-1] == -1:
            p[i][j-1] = (i, j)
            fringe.append((i,j-1))
    
    return(result, p, cells)

def lim_repeated_BFS(grid, dim):
    
    start = timeit.default_timer()
    
    dis = [[0 for i in range(dim)] for j in range(dim)]
    
    si = 0
    sj = 0

    result = False
    done = False
    
    final = []
    
    cells = 0
    
    while done != True:
        
        result, parent, BFS_cells = BFS(dim, dis, si, sj)
        cells = BFS_cells + cells
        
        if result == False:
            break
        
        path = find_path(parent, dim, si, sj)
        
        flag = True
        for (i, j) in path:
            if grid[i][j] == 1:
                dis[i][j] = 1
                (si, sj) = parent[i][j]
                final.pop(len(final)-1)
                flag = False
                break
            final.append((i, j))
        
        if flag:
            done = True
    
    stop = timeit.default_timer()
    
    return(result, final, dis, cells, start, stop)

df = pd.DataFrame(columns=['p',
                           'Trajectory Length',
                           'FDG Length',
                           'FG Length',
                           'Cells Processed'])

p = 0

x = 0

while p < 0.31:
    
    grid = gen_grid(101, p)
    
    result, traj, dis, cells_processed, start, stop = lim_repeated_BFS(grid, 101)
    
    if result:
        x = x + 1
        result, parent, c = BFS(101, dis, 0, 0)
        FDG_path = find_path(parent, 101, 0, 0)
        
        result, parent, c = BFS(101, grid, 0, 0)
        FG_path = find_path(parent, 101, 0, 0)
        
        df1 = pd.DataFrame([[p, len(traj), len(FDG_path), len(FG_path), cells_processed]],columns=['p','Trajectory Length','FDG Length','FG Length','Cells Processed'])
        df = pd.concat([df,df1])

    if x == 30:
        x = 0
        print(p)
        p = p + 0.01
        df.to_csv('Extra_Question_7.csv')
