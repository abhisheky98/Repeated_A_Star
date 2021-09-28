from Grid_Generator import gen_grid
import timeit

def find_path(parent, dim, si, sj): #used to find the path from the parent data structure
    i,j = dim-1, dim-1
    path = [(dim-1, dim-1)]
    while (i, j) != (si, sj):
        path.insert(0, parent[i][j])
        (i, j) = parent[i][j]
    return(path)

def BFS(dim, grid, si, sj):
    
    result = False
    
    fringe = [(si, sj)] #pushing the start node into the fringe
    cells = 0
    
    p = [[-1 for i in range(dim)] for j in range(dim)] #data structure to store pointers to parent (list of lists). initialized with -1 for now
    p[si][sj] = 0
    
    while len(fringe) != 0:
        (i, j) = fringe.pop(0)
        cells = cells + 1
        #print("a")
        if (i, j) == (dim-1, dim-1): #true if goal node is reached
            result = True
            break
        if i-1 >= 0 and grid[i-1][j] != 1 and p[i-1][j] == -1:
            p[i-1][j] = (i, j)
            fringe.append((i-1,j)) #insertion made in the end
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

def repeated_BFS(grid, dim):
    
    start = timeit.default_timer() #recording time stamp to measure run time
    
    dis = [[0 for i in range(dim)] for j in range(dim)] #used to represent the gridworld that has been discovered (list of lists)
    
    si = 0 #Co-ordinates of the start node
    sj = 0

    result = False
    done = False
    
    final = [] #Data structure to store final trajectory
    
    cells = 0
    
    while done != True:
        
        result, parent, BFS_cells = BFS(dim, dis, si, sj) #planning stage of repeated BFS
        cells = BFS_cells + cells #used to record total number of cells processed
        
        if result == False: #true if grid not solvable
            break
        
        path = find_path(parent, dim, si, sj)
        
        flag = True
        for (i, j) in path: #agent traversing the planned path
            try:
                dis[i-1][j] = grid[i-1][j] #recording the discovered grid
            except:
                pass
            try:
                dis[i][j+1] = grid[i][j+1]
            except:
                pass
            try:
                dis[i+1][j] = grid[i+1][j]
            except:
                pass
            try:
                dis[i][j+1] = grid[i][j+1]
            except:
                pass
            if grid[i][j] == 1: #true if current planned path has blocks
                dis[i][j] = 1
                (si, sj) = parent[i][j]
                final.pop(len(final)-1)
                flag = False
                break
            final.append((i, j))
        
        if flag:
            done = True
    
    stop = timeit.default_timer() #recording time stamp to measure run time
    
    return(result, final, dis, cells, start, stop)

##dim = 10
##grid = gen_grid(dim, 0.1)
##
##for x in grid:
##    print(x)
##
##result, parent, x = BFS(dim, grid, 0, 0)
##for x in parent:
##    print(x)
##
##path = find_path(parent, dim, 0, 0)
##print(path)
##
##result, final, dis, cells, start, stop = repeated_BFS(grid, dim)
##
##print("________________________________________________")
##print(result)
##print("Dis", dis)
##print("Cells", cells)
##print("Final", final)
