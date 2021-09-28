from Grid_Generator import gen_grid
from A_Star import a_star
import pandas as pd

df = pd.DataFrame(columns=['p','Solvable']) #made use of pandas library to store data

p=0.01

while p < 1: #recording values between 0.01 <= p < 1
    for i in range(100): #recording 100 values for each density value
        grid=gen_grid(101,p)
        result, start, stop, parent = a_star(101, p, grid, 1)
        df1 = pd.DataFrame([[p, result]],columns=['p', 'Solvable'])
        df = pd.concat([df, df1])
    df.to_csv('Question_4.csv')
    print(p)
    p = p + 0.01
