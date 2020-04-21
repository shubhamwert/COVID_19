import requests as req
import bs4 as bs
import pandas as pd

def updateData():
    page=req.get('https://www.mohfw.gov.in/')
    page.headers

    page.content.decode()
    a=bs.BeautifulSoup(page.content.decode())
    tb=a.find(lambda tag: tag.name=='table')
    rows=tb.findAll(lambda tag:tag.name=='tr')

    len(rows)

    Headers=rows[0].findAll(lambda tag:tag.name=='th')
    m=[]
    for i in Headers:
        m.append(i.text)

    Headers=m

    data=[]

    data.append(Headers)

    for i in range(1,len(rows)):
        row_data=[]
        row_data_raw=rows[i].findAll(lambda tag:tag.name=='td')
        if(len(row_data_raw)>0):
            for p in row_data_raw:
                row_data.append(p.text)
            data.append(row_data)

    #AUTOMATE THIS
    data[-3][1]=data[-3][1][0:-1]
    data[-3][2]=int(data[-3][2])
    data[-3][3]=int(data[-3][3])

    df=pd.DataFrame(data[1:-3],columns=Headers)

    df.to_csv('state_wise_corona_cases.csv')
    df.to_json('data.json',orient='records')

def WorldDataUpdate():
    page=req.get('https://www.worldometers.info/coronavirus/')
    page_data_full=bs.BeautifulSoup(page.content.decode())
    tb=page_data_full.find(lambda tag: tag.name=='table')
    rows=tb.findAll(lambda tag:tag.name=='tr')
    len(rows)
    Headers=rows[0].findAll(lambda tag:tag.name=='th')
    m=[]
    for i in Headers:
        m.append(i.text)

    Headers=m

    data=[]

    data.append(Headers)

    for i in range(1,len(rows)):
        row_data=[]
        row_data_raw=rows[i].findAll(lambda tag:tag.name=='td')
        if(len(row_data_raw)>0):
            for p in row_data_raw:
                row_data.append(p.text)
            data.append(row_data)

    a=pd.DataFrame(data=data)
    a.info()
    a.duplicated()
    a.to_csv("../data/country_data.csv")
    a.to_json('../data/country_data.json',orient='records')
