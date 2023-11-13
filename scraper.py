import pandas as pd

import matplotlib.pyplot as plt
import psycopg2
import requests
from bs4 import BeautifulSoup

def imdb_scraper():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    url = "https://osp.stat.gov.lt/statistiniu-rodikliu-analize?indicator=S3R0037#/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    ligos = soup.find_all("li", class_="ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent")

    # sarasas = []

    pavadinimas = []
    metai = []
    trukme = []
    vertinimas = []
    for  in ligos:
        title = movie.find("h3", class_="ipc-title__text").text.strip()
        pavadinimas.append(title)
        years = movie.find("span", class_="sc-c7e5f54-8 hgjcbi cli-title-metadata-item").text.strip()
        metai.append(years)
        length = movie.find("div", class_="sc-c7e5f54-7 brlapf cli-title-metadata").text.strip()[4:10]
        trukme.append(length)
        rating = movie.find("span",
                            class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")\
        .text.strip().replace("\xa0", " ")[0:3]
        vertinimas.append(rating)

        # sarasas.append((title, years, length, rating))

    data = {"Filmo_pavadinimas": pavadinimas,
            "Metai": metai,
            "Trukmė": trukme,
            "Vertinimas": vertinimas
    }

    df = pd.DataFrame(data)
    df1 = df
    # print(df1)

def df1():
    return None

    # return pavadinimas

    # print(response.status_code)
imdb_scraper()
