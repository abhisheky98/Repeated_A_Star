from Smart_Repeated_A_Star import smart_repeated_a_star
from Repeated_A_Star import repeated_a_star
from Grid_Generator import gen_grid
import pandas as pd

df = pd.DataFrame(columns=['p',
                           'Smart_time',
                           'Normal_time',
                           'Smart_length',
                           'Normal_length'])

p = 0.11
x = 0

while p<0.31:

    x= x + 1

    grid = gen_grid(101, p)

    result, path, dis, cells, start, stop = smart_repeated_a_star(grid, 101, p, 2)

    if result:

        Smart_t = stop-start
        Smart_l = len(path)

        result, path, dis, cells, start, stop = repeated_a_star(grid, 101, p, 2)

        Normal_t = stop-start
        Normal_l = len(path)

        #x = x + 1

        df1 = pd.DataFrame([[p, Smart_t, Normal_t, Smart_l, Normal_l]],columns=['p','Smart_time','Normal_time','Smart_length','Normal_length'])
        df = pd.concat([df,df1])

    if x==100:
        x = 0
        print(p)
        p = p + 0.05
        df.to_csv('Question_8.csv')

df.to_csv('Question_8.csv')
