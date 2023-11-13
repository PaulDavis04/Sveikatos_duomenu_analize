import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import psycopg2
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    'value': 'application/json, text/plain, */*',
    'accept': 'application/json, text/plain, */*',
    'cookie': '_ga=GA1.2.1272715160.1699462284; _gid=GA1.2.1647336826.1699462284; _ga_E8WJ6X0RYN=GS1.2.1699471615.3.0.1699471615.60.0.0; _ga_162SQ74LLR=GS1.2.1699471697.2.1.1699471698.0.0.0'
}
url = "https://osp.stat.gov.lt/analysis-portlet/services/api/v1/data/generate/table/hash/4b9681f1-aa53-47ad-832b-ef4b56eb3a22"
page = requests.get(url, headers=headers)
ilgis = len(page.json()["data"]["itemMatrix"])
sarasas1 = []
sarasas2 = []
sarasas3 = []
sarasas4 = []
sarasas5 = []
sarasas6 = []
# sarasas7 = []
# sarasas8 = []
for i in range(ilgis):
    try:

        data1 = page.json()["data"]["itemMatrix"][i][0]["value"]
        data2 = page.json()["data"]["itemMatrix"][i][1]["value"]
        data3 = page.json()["data"]["itemMatrix"][i][2]["value"]
        data4 = page.json()["data"]["itemMatrix"][i][3]["value"]
        data5 = page.json()["data"]["itemMatrix"][i][4]["value"]
        vyrai_moterys = page.json()["data"]["sidebar"][0]["captions"][i]["name"]
        # vyrai = page.json()["data"]["sidebar"][1]["captions"][i]["name"]
        # moterys = page.json()["data"]["sidebar"][2]["captions"][i]["name"]

    except KeyError:
            continue

    sarasas1.append(data1)
    sarasas2.append(data2)
    sarasas4.append(data3)
    sarasas5.append(data4)
    sarasas6.append(data5)


    sarasas3.append(vyrai_moterys)
    # sarasas7.append(vyrai)
    # sarasas8.append(moterys)
    # print(vyrai_moterys, data1, data2, data3, data4, data5)
#
    data = {
    "Pavadinimai": sarasas3,
    "2018": sarasas1,
    "2019": sarasas2,
    "2020": sarasas4,
    "2021": sarasas5,
    "2022": sarasas6
    }
    df = pd.DataFrame(data)
    print(df)
# # df[""] = df[""].str.split(pat='M', n=0, expand=True)[0]
# # df[""] = df[""].str.split(pat='M', n=0, expand=True)[1]
# # df.drop(columns=[''], inplace=True)
# # df = df.reindex(columns=['', 'Month', '', ''])
# # print(df)
# # df.to_csv("LIGOS.csv", index=True)