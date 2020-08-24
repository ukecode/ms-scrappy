import requests
from bs4 import BeautifulSoup


def get_value(soup):
    value = soup.find('div', {"class": "value"})
    value = value.find('p')
    return float(value.text.replace(",", "."))


def get_variation_day(soup):
    value = soup.find('div', {"class": "percentage"})
    value = value.find('p')
    return value.text.replace(",", ".").strip()


def listAcoes(acoes):
    result = []
    for acao in acoes:
        url = "https://www.infomoney.com.br/cotacoes/" + str(acoes[acao])
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')

        if (acao in ["EURO","DOLAR"]):
            ret = {
                "name": acao,
                "value": get_exchange(acoes[acao]),
                "variation_day": 0
            }
        else: 
            ret = {
                "name": acao,
                "value": get_value(soup),
                "variation_day": get_variation_day(soup)
            }

        result.append(ret)
    return result

def getId(soup, id):
    value = soup.find('id', id)
    return value

def getInput(soup, input):
    value = soup.find('input', input)
    return value

def get_exchange(coin):
    url = "https://economia.uol.com.br/cotacoes/cambio/" + coin
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    my_input = {"class": "field normal", "name":"currency2" }
    ret =  getInput(soup, my_input)['value']
    return float(ret.replace(",","."))


