from Repeated_A_Star import repeated_a_star
from Repeated_BFS import repeated_BFS
from Grid_Generator import gen_grid
import pandas as pd

df = pd.DataFrame(columns=['p', 'BFS Time', 'A* Time'])

p = 0.01
x = 0

while p<0.31:
    grid =  gen_grid(101, p)
    result, final, dis, cells, start, stop = repeated_BFS(grid, 101)
    if result:
        b = stop-start
        result, final, dis, cells, start, stop = repeated_a_star(grid, 101, p, 2)
        a = stop-start
        df1 = pd.DataFrame([[p, b, a]], columns=['p', 'BFS Time', 'A* Time'])
        df = pd.concat([df, df1])
        x = x + 1
    if x==30:
        x = 0
        print(p)
        p = p + 0.01
        df.to_csv('Extra.csv')
