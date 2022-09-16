import requests
from bs4 import BeautifulSoup as BS

def weather():
    url = 'https://world-weather.ru/pogoda/russia/anapa/'

    response = requests.get(url)
    soup = BS(response.text, 'lxml')

    weather = ''
    soup = soup.find('div', class_='weather-now-info')
    teg_p = soup.find('p')
    print(soup)
    time = teg_p.find('b')
    #temp = soup.find_('//*[@id="weather-now-number"]/text()')
    titile = soup.find('span').attrs.get('title')
    time = 'Сейчас в Анапе:\n' + time.get_text()
    print(titile)


weather()
