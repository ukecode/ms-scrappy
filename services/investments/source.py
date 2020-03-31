import requests
from bs4 import BeautifulSoup

def get_value(soup):
    value = soup.find('div', {"class": "value"})
    value = value.find('p')
    return float(value.text.replace(",","."))

def get_variation_day(soup):
    value = soup.find('div', {"class": "percentage"})
    value = value.find('p')
    return value.text.replace(",",".").strip()


def listAcoes(acoes):
    result = []
    for acao in acoes:
        url = "https://www.infomoney.com.br/cotacoes/" + str(acoes[acao])
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')

        ret = {
            "name": acao,
            "value": get_value(soup),
            "variation_day": get_variation_day(soup)
        }

        result.append(ret)
    return result