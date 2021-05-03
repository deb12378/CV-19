import requests
from bs4 import BeautifulSoup
import csv
def rows_for_csv(L):
    L1,L2=[],[];k=""
    for i in L:
        L1=[];f=0
        for j in i:
            if ord(j)>=32:
                k+=j
                f=0
            else:
                f+=1
                if k!="":
                    L1.append(k)
                    k=""
                if f>1:
                    L1.append(0)
            if len(L1) == 17:
                break
        L2.append(L1)
    return L2

page=requests.get("https://www.worldometers.info/coronavirus/")
soup=BeautifulSoup(page.content,'html.parser')
x=soup.find(id="main_table_countries_today")
rows=[i.text for i in x.find_all('tr')[9:224]]
n=[i[0:-1] for i in rows_for_csv(rows)]
fr=["SL.NO","COUNTRY","TOTAL CASES","NEW CASES","TOTAL DEATHS","NEW DEATHS","TOTAL RECOVERED","NEW RECOVERED","ACTIVE CASES","CRITICAL CASES","CASES/MILLION","DEATHS/MILLION","TOTAL TESTS","TESTS/MILLION","POPULATION","CONTINENT"]
n.insert(0,fr)
with open('data.csv', 'w+', newline='') as d:
    writer = csv.writer(d)
    writer.writerows(n)
