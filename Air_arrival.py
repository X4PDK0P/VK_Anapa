import requests
from bs4 import BeautifulSoup as BS

def arrival():
    url = 'https://rasp.yandex.ru/informers/station/9623572?color=1&event=arrival&size=25&type=tablo'

    response = requests.get(url)
    soup = BS(response.text, 'lxml')

    flight = ''
    rows = soup.findAll('tr', {'class': 'StationInformerPlaneTableRowDesktop StationInformerPlaneTableRowDesktop_color_default'})
    rows = soup.find_all('tr')
    for tr in rows:
        time = tr.find('span', class_='StationInformerPlaneTableRowDesktop__scheduledTime')
        try:
            flight = flight + ' | ' + time.get_text()
        except:
            pass
        city = tr.find('td', class_='StationInformerPlaneTableRowDesktop__directionColumn')
        try:
            flight = flight + ' | ' + city.get_text()
        except:
            pass
        plane = tr.find('div', class_='StationInformerPlaneTableRowDesktop__threadNumber')
        try:
            flight = flight + ' | ' + plane.get_text()
        except:
            pass
        plane_name = tr.find('div', class_='StationInformerPlaneTableRowDesktop__companyTitleLink')
        try:
            flight = flight + ' ' +plane_name.get_text()
        except:
            pass
        status = tr.find('td', class_='StationInformerPlaneTableRowDesktop__statusColumn')
        try:
            flight = flight + ' | ' + status.get_text() + ' |\n\n'
        except:
            pass
    flight += url
    #print(flight)
    return flight
