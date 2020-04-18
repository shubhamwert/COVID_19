import pandas as pd


df=pd.read_csv('state_wise_corona_cases.csv')

df.head()

df=df.drop([df.columns[0],df.columns[1]],axis=1)

df.hist()
a=df.plot.bar()

