# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:44:05 2021

@author: Abhishek
"""

from Grid_Generator import gen_grid
import timeit
import pandas as pd 
import csv

def dist(i, j, dim, heu):
    if heu == 1:
        return ( ((i-dim-1) ** 2) + ((j-dim-1) ** 2) ) ** 0.5
    if heu == 2:
        return abs(dim-1-i)+abs(dim-1-j)
    if heu == 3:
        return max(abs(i-dim-1),abs(j-dim-1))
    if heu == 4:
        return ((( ((i-dim-1) ** 2) + ((j-dim-1) ** 2) ) ** 0.5)+(abs(dim-1-i)+abs(dim-1-j))+( max(abs(i-dim-1),abs(j-dim-1))))

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

def a_star(dim, grid, heu, si, sj,w): # used w as a factor applied to the heuristic
    
    result=False
    
    g=[[-1 for i in range(dim)] for j in range(dim)]
    g[si][sj]=0
    
    h=[[dist(i,j,dim,heu)*w for i in range(dim)] for j in range(dim)]  # heurestic multiplied by factor w 
    
    
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
            f[i-1][j]=g[i-1][j]+(h[i-1][j])
            insert_fringe(i-1,j,fringe,f)
            
        if j+1 < dim and grid[i][j+1] != 1 and p[i][j+1]==-1 and p[i][j] != (i,j+1):
            p[i][j+1]=(i,j)
            g[i][j+1]=g[i][j]+1
            f[i][j+1]=g[i][j+1]+(h[i][j+1])
            insert_fringe(i,j+1,fringe,f)
            
        if i+1 < dim and grid[i+1][j] != 1 and p[i+1][j]==-1 and p[i][j] != (i+1,j):
            p[i+1][j]=(i,j)
            g[i+1][j]=g[i][j]+1
            f[i+1][j]=g[i+1][j]+(h[i+1][j])
            insert_fringe(i+1,j,fringe,f)
            
        if j-1 >= 0 and grid[i][j-1] != 1 and p[i][j-1]==-1 and p[i][j] != (i,j-1):
            p[i][j-1]=(i,j)
            g[i][j-1]=g[i][j]+1
            f[i][j-1]=g[i][j-1]+(h[i][j-1])
            insert_fringe(i,j-1,fringe,f)
    
    return(result, p)

def repeated_a_star(grid, dim,  heu,w):
    
    start = timeit.default_timer()
    
    dis = [[0 for i in range(dim)] for j in range(dim)]
    
    result = False
    done = False
    
    si = 0
    sj = 0
    
    final = []
    
    cells = 0
    
    while done != True:
        
        result, parent =a_star(dim, dis, heu, si, sj,w)
        if result == False:
            break
        
        path = find_path(parent, dim, si, sj)
        cells = cells + search_size(parent, dim)
        
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
    
    stop = timeit.default_timer()
    
    return(result, final, dis, cells, start, stop)

df = pd.DataFrame(columns=['w value ', 'Result ', 'Time taken ', 'heuristic type'])

                

#Loop run on same grid for all heurestic , values of w varied .

grid=gen_grid(101, 0.3)
count=0
h=0
w=0.8
#for w in range (1,5,0.2):
while (w<3):
    w+=0.2
    print("helo")
    for h in range(1,5):
        
        print("loops", h)
    
        
        print(h)
        count=0
        while(count<10):
            
            result , f, d, c ,s , st = (repeated_a_star(grid, 101, h,w))
            tim=st-s
            count+=1
            print(result,tim)
            print(w)
            two=2
            df=df.append({'w value':w , 'Result': result , 'Time taken': tim , 'heuristic type':h , 'path length ':len(f),'p value':0.2}, ignore_index=True)
        
df.to_csv('Question_9_p(0.4.1).csv')
        