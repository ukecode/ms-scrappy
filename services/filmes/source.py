import requests
from bs4 import BeautifulSoup


def trata_filme(filme):
    img = filme.find('img')
    a = filme.find('a')
    nome = img['alt']
    img = img['src']
    url = a['href']
    result = {
        "nome": nome,
        "img": img,
        "url": url
    }

    return result


def result():
    result = []
    url = "http://www.megatorrentshd.org/"
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')

    filmes = soup.find_all('div', {'class': 'ItemN'})
    result = []
    for filme in filmes:
        result.append(trata_filme(filme))
    return {"data": result}
