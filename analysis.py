import pandas as pd
import pygal 

df=pd.read_csv('data/state_wise_corona_cases.csv')

df.head()

df=df.drop([df.columns[0],df.columns[1]],axis=1)

df.hist()
a=df.plot.bar()
df=df.sort_values(by=df.columns[1])

def createSvgStateWise(n=0):
    if(n==0):
        n=df.shape[1]
    p=df.tail(n)
    a=pygal.Bar()
    a.x_labels=p[p.columns[0]]
    a.title="State Wise Plot of Covid 19"
    for i in range(1,p.shape[1]):
        a.add(p.columns[i],p[p.columns[i]])
    return a

