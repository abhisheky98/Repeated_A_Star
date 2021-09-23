import pandas as pd

df = pd.DataFrame(columns=['p', 'Solvability'])

record = pd.read_csv('Question_4.csv')

x = 0
p = 0.01
ans = 0

for index, row in record.iterrows():
    #print(row['p'], row['Solvable'])
    x = x + 1
    if row['Solvable']:
        ans = ans + 1
    if x==100:
        d = pd.DataFrame([[p, ans]], columns=['p', 'Solvability'])
        df = pd.concat([df,d])
        df.to_csv('Question_4_analysis.csv')
        x = 0
        p = p + 0.01
        ans = 0
