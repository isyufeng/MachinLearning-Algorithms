# Exercise in L11

import numpy as np
import pandas as pd

df = pd.read_csv('task.csv')
#remane the columns
new_name = {'food': 'Food Name', 'ounces': 'Ounces', 'animal': 'Animal'}
df.rename(columns=new_name, inplace=True)
print(df)
#replace the illegal value column of Ounces
df['Ounces'].replace(-3,3)
#fill the NaN value in column of Ounces
df['Ounces'].fillan(df['Ounces'].mean(), inplace=True)
print(df)
#convert the first character into uppercase in column of Food Name
df['Food Name'].Series.str.capitalize()
df.to_csv('task_modified.csv')

