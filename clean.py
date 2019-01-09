# Exercise in L11

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('task.csv')
# print(df['ounces'])
# print(df['ounces'].isnull())
#remane the columns
new_name = {'food': 'Food Name', 'ounces': 'Ounces', 'animal': 'Animal'}
df.rename(columns=new_name, inplace=True)
print(df)
print('-----Final output---------')
#replace the illegal value column of Ounces
df.loc[6,'Ounces']=3.0
# fill the NaN value in column of Ounces
df['Ounces'].fillna(df['Ounces'].mean(), inplace=True)
#print(df)
# convert the first character into uppercase in column of Food Name
df['Food Name'] = df['Food Name'].str.title()
df['Animal'] = df['Animal'].str.title()
print(df)
#df.to_csv('task_modified.csv')

