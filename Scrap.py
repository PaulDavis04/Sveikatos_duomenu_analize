import pandas as pd
import psycopg2
import requests
from bs4 import BeautifulSoup
import json

#---
# def originali_lentele():
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    'accept': "application/json, text/plain, */*",
    'cookie': 'COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=lt_LT; _ga_FMWT2SD2FH=GS1.1.1699779108.9.1.1699779383.0.0.0; _ga=GA1.3.1923789538.1699618794; _gid=GA1.3.1435366625.1699618794; JSESSIONID=94DC126A5404F74B352AF282520E0BEF.osp-bDSgBvYc1d; LFR_SESSION_STATE_10158=1699779383392; _gat=1'
}
url = "https://osp.stat.gov.lt/statistiniu-rodikliu-analize?indicator=S3R0037#/"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
ilgis = len(page.json()["data"]["itemMatrix"])

sarasas1 = []
sarasas2 = []
sarasas3 = []
sarasas4 = []
sarasas5 = []


for i in range(ilgis):
    data1 = page.json()["data"]["itemMatrix"][i][0]["value"]
    [sarasas1].append(data1)
    data2 = page.json()["data"]["itemMatrix"][i][1]["value"]
    [sarasas2].append(data2)
    data3 = page.json()["data"]["itemMatrix"][i][2]["value"]
    [sarasas3].append(data3)
    data4 = page.json()["data"]["itemMatrix"][i][3]["value"]
    [sarasas4].append(data4)
    data5 = page.json()["data"]["itemMatrix"][i][4]["value"]
    [sarasas5].append(data5)
    print(data1)
data["2018"].append(data1)
print(data)

data = {
    "2018": sarasas1,
    "2019": sarasas2,
    "2020": sarasas3,
    "2021": sarasas4,
    "2022": sarasas5
}

print(data)
df = pd.DataFrame(data)
print(df)
df.to_csv("Ligos.csv", index=True)
print(page.status_code)


# originali_lentele()