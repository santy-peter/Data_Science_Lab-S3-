#1
import pandas as pd
names = ['santy','pournami','athulya']
x = pd.Series(names)
print(names)
print(x)


#2
import pandas as np
sr = pd.date_range('2021-05-01','2021-05-12',freq = 'D')
x=pd.Series(sr)
#print(x)
print(x.to_string(index=False))

#3
import pandas as pd

d = {
    'Name' : ['santy','pournami','athulya'],
    'Age' : [23,24,22],
    'Course':['MCA','MCA','MCA'],
}
df = pd.DataFrame(d)
print(df.to_string(index=False))


#4

import pandas as pd
a=[[11,12],[14,15]]
b=pd.DataFrame(a)
print(b)


#5

import pandas as pd
df = pd.read_csv('5.csv')
print(df.to_string()) 


#6

import pandas as pd
df = pd.DataFrame({'Name': ['santy','pournami','athulya','aish','rahul','ann'],
                   'Age': [23,24,22,22,21,13],
                   'Rank': [0,1,2,3,4,5]})

print(df.to_string())
print('SORTED DATAFRAME BY NAME ')
df = df.sort_values(by=['Name'], ascending=[True])
print(df.to_string())
print('SORTED DATAFRAME BY AGE ')
df = df.sort_values(by=['Age'], ascending=[True])
print(df.to_string())



#7

import pandas as pd
data = {'Name': ['santy','pournami','athulya','aish','rahul','ann'],
                   'Age': [23,24,22,22,21,13],
                   'Rank': [0,1,2,3,4,5],}
index = ['a1', 'b1', 'c1', 'd1', 'e1','f1']
df = pd.DataFrame(data,index)
print(df.to_string())
df.reset_index(inplace = True, drop = True)
print(df.to_string())

#8

import pandas as pd
df = pd.DataFrame({'Name': ['santy','pournami','athulya','aish','rahul','ann'],
                   'Age': [23,24,22,22,21,13],
                   'Rank': [0,1,2,3,4,5]})
print(df[:2])


#9

import pandas as pd
df = pd.DataFrame({'Name': ['santy','pournami','athulya','aish','rahul','ann'],
                   'Occupation': ['teacher','doctor','engineer','teacher','doctor','vect'],
                   'Salary': [12000,35000,50000,14000,40000,30000]})

df = pd.DataFrame(df)
print(df)
avg = df.groupby('Occupation')['Salary'].mean()
print("  Average salary per occupation : ")
print(avg)


#10
import pandas as pd
import numpy as np

nums = {'Set_of_Numbers': [2, 3, np.nan, 7, 11, 13,np.nan, 19, 23, np.nan]}
df = pd.DataFrame(nums)
df = df.fillna(0)
print(df)

#11
import pandas as pd

details = {
    'cname' : ['deloitte','IBM','UST','Accenture'],
    'profit' : [24,25,0,-27],
}
df = pd.DataFrame(details)
df.loc[df.profit <= 0,'profit'] = False
df.loc[df.profit > 0,'profit'] = True
print(df)



#12
import pandas as pd
details_1 = {
    'eid' : [1,2,3,4],
    'ename' : ['ann','pournami','santy','athulya'],
    'stipend':[123,131,23,434],
}

details_2 = {
    'eid' : [1,2,3,4],
    'designation' : ['manager','analyst','tester','CEO'],
}

df_1 = pd.DataFrame(details_1)
df_2 = pd.DataFrame(details_2)

dataframe = pd.merge(df_1, df_2, how = 'inner', on = 'eid')
print(dataframe)
