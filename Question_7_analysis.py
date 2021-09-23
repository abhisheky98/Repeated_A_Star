import pandas as pd

df = pd.DataFrame(columns=['p', 'Avg Trajectory Length', 'Avg T_FDG', 'Avg FDG_FG', 'Avg Cells Processed'])

record = pd.read_csv('Question_7.csv')

traj = 0
T_FDG = 0
FDG_FG = 0
cells = 0

x = 0

for index, row in record.iterrows():
    x = x + 1
    traj = traj + row['Trajectory Length']
    T_FDG = T_FDG + (row['Trajectory Length'] / row['FDG Length'])
    FDG_FG = FDG_FG + (row['FDG Length'] / row['FG Length'])
    cells = cells + row['Cells Processed']

    if x == 100:
        df1 = pd.DataFrame([[row['p'], traj/100, T_FDG/100, FDG_FG/100, cells/100]], columns=['p', 'Avg Trajectory Length', 'Avg T_FDG', 'Avg FDG_FG', 'Avg Cells Processed'])
        df = pd.concat([df,df1])
        traj = 0
        T_FDG = 0
        FDG_FG = 0
        cells = 0
        df.to_csv('Question_7_analysis.csv')
        x = 0
