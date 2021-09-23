import pandas as pd

df = pd.DataFrame(columns=['Grid', 'Time_E', 'Search_Space_E', 'Path_Length_E', 'Time_M', 'Search_Space_M', 'Path_Length_M', 'Time_C', 'Search_Space_C', 'Path_Length_C'])

record = pd.read_csv('Question_5.csv')

i = 0
x = 0
dat = [0, 0, 0]

for index, row in  record.iterrows():
    i = i + 1
    print(i)
    dat[x] = {'Time':row['Time'],
              'Search_Space':row['Search Space'],
              'Path_Length':row['Path Length']}
    x = x + 1
    if x == 3:
        df1 = pd.DataFrame([[row['p'], row['Grid'], dat[0]['Time'], dat[0]['Search_Space'], dat[0]['Path_Length'], dat[1]['Time'], dat[1]['Search_Space'], dat[1]['Path_Length'], dat[2]['Time'], dat[2]['Search_Space'], dat[2]['Path_Length'] ]], columns=['p', 'Grid', 'Time_E', 'Search_Space_E', 'Path_Length_E', 'Time_M', 'Search_Space_M', 'Path_Length_M', 'Time_C', 'Search_Space_C', 'Path_Length_C'])
        df = pd.concat([df,df1])
        x=0
        df.to_csv('Question_5_analysis.csv')
        dat = [0, 0, 0]
