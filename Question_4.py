from Grid_Generator import gen_grid
from A_Star import a_star
import pandas as pd

df = pd.DataFrame(columns=['p','Solvable'])

p=0.01

while p < 1:
    for i in range(100):
        grid=gen_grid(101,p)
        result, start, stop, parent = a_star(101, p, grid, 1)
        df1 = pd.DataFrame([[p, result]],columns=['p', 'Solvable'])
        df = pd.concat([df, df1])
    df.to_csv('Question_4.csv')
    print(p)
    p = p + 0.01

##def find_path(parent, dim):
##    i,j = 100,100
##    path = [(100,100)]
##    while (i,j) != (0,0):
##        path.insert(0, parent[i][j])
##        (i,j) = parent[i][j]
##    return(path)
##
##df = pd.DataFrame(columns=['p',
##                           'Grid',
##                           'Solvable',
##                           'Start',
##                           'Stop',
##                           'Time',
##                           'Heuristic Function',
##                           'Parent',
##                           'Path',
##                           'Path Length'
##                           ])
##
##p=0.01
##while p < 1:
##    for i in range(100):
##        grid=gen_grid(101,p)
##        result, start, stop, parent = a_star(101, p, grid, 1)
##        if result==True:
##            path=find_path(parent, 101)
##        else:
##            path=[]
##        df1 = pd.DataFrame([[p,grid,result,start,stop,stop-start,"Euclidean",[parent],[path],len(path)-1]],columns=['p','Grid','Solvable','Start','Stop','Time','Heuristic Function','Parent','Path','Path Length'])#,ignore_index=True)
##        #df.append(df1,ignore_index=True)
##        df=pd.concat([df,df1])
##        df.append({'p':[p],
##                   'Grid':[grid],
##                   'Solvable':[result],
##                   'Start':[start],
##                   'Stop':[stop],
##                   'Time':[stop-start],
##                   'Heuristic Function':["Euclidean"]
##                   #'Parent':[0],
##                   #'Path':[0],
##                   #'Path Length':[len(path)-1]
##                   }, ignore_index=True)
##        #print(df)
##    df.to_csv('datafinal.csv')
##    print(p)
##    p = p + 0.01
##
##print(df)
##df.to_csv('datafinal.csv')
