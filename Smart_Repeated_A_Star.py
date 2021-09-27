import timeit

def dist(i, j, dim, heu):
    if heu == 1:
        return ( ((i-dim-1) ** 2) + ((j-dim-1) ** 2) ) ** 0.5
    if heu == 2:
        return abs(dim-1-i)+abs(dim-1-j)
    if heu == 3:
        return max(abs(i-dim-1),abs(j-dim-1))

def insert_fringe(i, j, fringe, f):
    #print(fringe)
    if len(fringe)==0:
        fringe.append((i,j))
    else:
        for x in range(len(fringe)):
            (I,J)=fringe[x]
            if f[I][J]>f[i][j]:
                fringe.insert(x, (i,j))
                return
        fringe.append((i,j))

def find_path(parent, dim, si, sj):
    i,j = dim-1, dim-1
    path = [(dim-1, dim-1)]
    while (i, j) != (si, sj):
        path.insert(0, parent[i][j])
        (i, j) = parent[i][j]
    return(path)

def search_size(parent, dim):
    ans = 0
    for i in parent:
        for j in i:
            if j == -1:
                ans = ans + 1
    return ((dim * dim) - ans)

def find_child(i, j, grid, dim):
    child = []
    if i-1 >= 0 and grid[i-1][j]!=1:
        child.append((i-1,j))
    if j+1 < dim and grid[i][j+1]!=1:
        child.append((i,j+1))
    if i+1 < dim and grid[i+1][j]!=1:
        child.append((i+1,j))
    if j-1 >= 0 and grid[i][j-1]!=1:
        child.append((i,j-1))
    return(child)

def a_star(dim, P, grid, heu, si, sj):
    
    result=False
    
    g=[[-1 for i in range(dim)] for j in range(dim)]
    g[si][sj]=0
    
    h=[[dist(i,j,dim,heu) for i in range(dim)] for j in range(dim)]
    
    f=[[-1 for i in range(dim)] for j in range(dim)]
    f[si][sj]=g[si][sj]+h[si][sj]
    p=[[-1 for i in range(dim)] for j in range(dim)]
    p[si][sj]=0
    
    fringe=[(si,sj)]
    
    while len(fringe)!=0:
        (i,j)=fringe.pop(0)
        if (i,j) == (dim-1,dim-1):
            result=True
            break
        #print((i,j))
        if i-1 >= 0 and grid[i-1][j] != 1 and p[i-1][j]==-1 and p[i][j] != (i-1,j):
            p[i-1][j]=(i,j)
            g[i-1][j]=g[i][j]+1
            f[i-1][j]=g[i-1][j]+h[i-1][j]
            insert_fringe(i-1,j,fringe,f)
            
        if j+1 < dim and grid[i][j+1] != 1 and p[i][j+1]==-1 and p[i][j] != (i,j+1):
            p[i][j+1]=(i,j)
            g[i][j+1]=g[i][j]+1
            f[i][j+1]=g[i][j+1]+h[i][j+1]
            insert_fringe(i,j+1,fringe,f)
            
        if i+1 < dim and grid[i+1][j] != 1 and p[i+1][j]==-1 and p[i][j] != (i+1,j):
            p[i+1][j]=(i,j)
            g[i+1][j]=g[i][j]+1
            f[i+1][j]=g[i+1][j]+h[i+1][j]
            insert_fringe(i+1,j,fringe,f)
            
        if j-1 >= 0 and grid[i][j-1] != 1 and p[i][j-1]==-1 and p[i][j] != (i,j-1):
            p[i][j-1]=(i,j)
            g[i][j-1]=g[i][j]+1
            f[i][j-1]=g[i][j-1]+h[i][j-1]
            insert_fringe(i,j-1,fringe,f)
    
    return(result, p)

def smart_repeated_a_star(grid, dim, P, heu):
    
    start = timeit.default_timer()
    
    dis = [[0 for i in range(dim)] for j in range(dim)]
    
    result = False
    done = False
    
    si = 0
    sj = 0
    
    final = []
    
    cells = 0
    
    while done != True:

        #print("start", si, sj)
        result, parent =a_star(dim, P, dis, heu, si, sj)
        if result == False:
            break
        
        path = find_path(parent, dim, si, sj)
        cells = cells + search_size(parent, dim)
        #print("path", path)
        flag = True
        for (i, j) in path:
            try:
                dis[i-1][j] = grid[i-1][j]
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
            if grid[i][j] == 1:
                dis[i][j] = 1
                (si, sj) = parent[i][j]
                final.pop(len(final)-1)
                flag = False
                break
            final.append((i, j))

        if flag:
            done = True
            break

        flag = True
        while flag and (si, sj) != (0,0):
            flag = True
            for child in find_child(si, sj, dis, dim):
                if child not in path:
                    flag = False
                    break
            if flag:
                final.append((si, sj))
                (si, sj) = parent[si][sj]
        #print("Final", final)
    
    stop = timeit.default_timer()
    
    return(result, final, dis, cells, start, stop)

