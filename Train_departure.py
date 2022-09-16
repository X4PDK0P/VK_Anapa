import requests
from bs4 import BeautifulSoup as BS

def departure():
    url = 'https://rasp.yandex.ru/informers/station/9613091?color=1&size=25&type=train'

    response = requests.get(url)
    soup = BS(response.text, 'lxml')

    train = ''
    rows = soup.findAll('tr', {'class': 'StationInformerPlaneTableRowDesktop StationInformerPlaneTableRowDesktop_color_default'})
    rows = soup.find_all('tr')
    for tr in rows:
        time = tr.find('td', class_='StationInformerRailroadTableRowDesktop__timeColumn')
        try:
            train = train + ' | ' + time.get_text()
        except:
            pass
        route = tr.find('div', class_='StationInformerRailroadTableRowDesktop__direction')
        try:
            train = train + ' | ' + route.get_text() + ' |\n\n'
        except:
            pass
    train += url
    #print(train)
    return train
