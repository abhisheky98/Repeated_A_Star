from Grid_Generator import gen_grid
from A_Star import a_star
import pandas as pd

##Parameters being recorded to compare heuristics
##Solvability
##Exeution time
##Search space pruned
##Optimal solution

def find_path(parent, dim): #used to find the path from the parent data structure
    i,j = dim-1, dim-1
    path = [(100,100)]
    while (i,j) != (0,0):
        path.insert(0, parent[i][j])
        (i,j) = parent[i][j]
    return(path)

def search_size(parent, dim): #used to find the size of the search tree that was discovered
    ans = 0
    for i in parent:
        for j in i:
            if j == -1:
                ans = ans + 1
    return ((dim * dim) - ans)

df = pd.DataFrame(columns=['p',
                           'Grid',
                           'Start',
                           'Stop',
                           'Time',
                           'Heuristic Function',
                           'Search Space',
                           'Path Length'
                           ]) #used pandas library to record data

p=0.01
while p < 0.31: #recording values between 0.01 <= p < 0.31
    for i in range(100):
        grid = gen_grid(101,p)
        result, start, stop, parent = a_star(101, p, grid, 1)
        if result == True:
            path = find_path(parent, 101)
            searchs = search_size(parent, 101)
            df1 = pd.DataFrame([[p, grid, start, stop, stop-start, "Euclidean", searchs, len(path)]],columns=['p', 'Grid','Start','Stop','Time','Heuristic Function','Search Space','Path Length'])
            df = pd.concat([df,df1])
            
            result, start, stop, parent = a_star(101, p, grid, 2)
            path = find_path(parent, 101)
            searchs = search_size(parent, 101)
            df1 = pd.DataFrame([[p, grid, start, stop, stop-start, "Manhattan", searchs, len(path)]],columns=['p', 'Grid','Start','Stop','Time','Heuristic Function','Search Space','Path Length'])
            df = pd.concat([df,df1])
            
            result, start, stop, parent = a_star(101, p, grid, 3)
            path = find_path(parent, 101)
            searchs = search_size(parent, 101)
            df1 = pd.DataFrame([[p, grid, start, stop, stop-start, "Chebyshev", searchs, len(path)]],columns=['p', 'Grid','Start','Stop','Time','Heuristic Function','Search Space','Path Length'])
            df = pd.concat([df,df1])
    df.to_csv('Question_5.csv')
    print(p)
    p = p + 0.01
